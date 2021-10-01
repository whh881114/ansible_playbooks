#!/usr/bin/python
# -*- coding: UTF-8 -*-


import logging
import argparse
import subprocess

HARBOR_SERVER = "harbor.freedom.org"
ALI_REGISTER = "registry.aliyuncs.com/google_containers"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def pull_image(image):
    if LOCAL_REGISTER:
        image = HARBOR_SERVER + "/" + image
    try:
        cmd = subprocess.Popen("docker pull %s" % image, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        cmd.wait()
        logger.info("Pull docker image \"%s\" successfully." % image)
    except Exception as e:
        logger.error("Pull docker image \"%s\" failed. The error is %s." % (image, e))


def push_image(image):
    try:
        local_register_image = HARBOR_SERVER + "/" + image
        cmd = subprocess.Popen("docker tag %s %s" % (image, local_register_image), stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=True)
        cmd.wait()
        image = local_register_image
        cmd = subprocess.Popen("docker push %s" % image, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        cmd.wait()
        logger.info("Push docker image \"%s\" successfully." % image)
    except Exception as e:
        logger.error("Push docker image \"%s\" failed. The error is %s." % (image, e))


def action_images(images, action):
    if action == "push":
        for image in images:
            push_image(image)
    else:
        for image in images:
            pull_image(image)


def file_images(files, action):
    images = []
    for file in files:
        with open(file, "r") as f:
            tmp_images = f.readlines()
            for img in tmp_images:
                # 去掉空格
                img = img.strip(" ")
                # 去掉以#开头注释及换行
                if img[0] == "#" or img == "\n":
                    pass
                # 当#位于镜像后处理逻辑
                elif img.find("#"):
                    img = img.split("#")
                    img = img[0]
                    img = img.strip(" ")
                    img = img.replace("\n", "").replace("\r", "")
                    images.append(img)
                else:
                    img = img.replace("\n", "").replace("\r", "")
                    images.append(img)
    action_images(images, action)


def k8s_images(k8s_versions, action):
    for version in k8s_versions:
        ret = subprocess.Popen("kubeadm config images list --kubernetes-version %s" % version,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        for img in ret.stdout:
            img = img.replace("\n", "").replace("\r", "")
            original_img = img.split("/")
            ali_img = ALI_REGISTER + "/" + original_img[-1]
            if action == "pull":
                pull_image(ali_img)
                # 下载k8s镜像后，还需要重新打个tag
                cmd = subprocess.Popen("docker tag %s %s" % (ali_img, original_img), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                cmd.wait()
            else:
                harbor_img = HARBOR_SERVER + "/k8s.gcr.io" + original_img[-1]
                push_image(harbor_img)


def main():
    parser = argparse.ArgumentParser(description="Clients download docker images using the parameters as below.")

    parser.add_argument("-f", "--files", type=str,
                        help="Specify the files containing docker images to pull. When specify multi ones, "
                             "plase use comma to sperate them.")

    parser.add_argument("-v", "--k8s_versions", type=str,
                              help="Specify the kubernetes docker images to pull that the script downloads "
                                   "the docker images of these versions. When specify multi ones, "
                                    "plase use comma to sperate them.")
    parser.add_argument("-a", "--action", type=str, choices=["pull", "push"], default="pull",
                              help="Which action to be executed and the default value is pull.")

    parser.add_argument("-l", "--local", type=bool, default=False, help="Download docker images from local register or not.")

    args = parser.parse_args()

    files = args.files
    k8s_versions = args.k8s_versions
    action = args.action
    global LOCAL_REGISTER
    LOCAL_REGISTER = args.local

    if len(files) == 0:
        pass
    else:
        files = files.split(",")
        file_images(files, action)

    if len(k8s_versions) == 0:
        pass
    else:
        k8s_versions = k8s_versions.split(",")
        k8s_images(k8s_versions, action)


if __name__ == "__main__":
    main()