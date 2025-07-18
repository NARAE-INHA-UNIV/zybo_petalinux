# Petalinux Build

[[Docs] 0. Vivado & PetaLinux Build 환경 구축](../docs/0_Vivado_Petalinux_Install.md)

## Steps

### 1. 프로젝트 생성

```bash
$ source /opt/pkg/petalinux/settings.sh
*************************************************************************************************************************************************
The PetaLinux source code and images provided/generated are for demonstration purposes only.
Please refer to https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/2741928025/Moving+from+PetaLinux+to+Production+Deployment
 for more details
*************************************************************************************************************************************************
PetaLinux environment set to '/opt/pkg/petalinux'
WARNING: /bin/sh is not bash!
bash is PetaLinux recommended shell. Please set your default shell to bash.
[WARNING] This is not a supported OS
[INFO] Checking free disk space
[INFO] Checking installed tools
[INFO] Checking installed development libraries
[INFO] Checking network and other services
[WARNING] No tftp server found - please refer to "UG1144 2024.2 PetaLinux Tools Documentation Reference Guide" for its impact and solution
```

bash 관련 경고는 WSL이라 그런 듯 하다.

아래 명령을 통해 프로젝트를 생성한다.
```bash
petalinux-create --type project --template zynq --name petalinux
cd petalinux
```

xsa 파일을 통해 HW 구성을 반영한다. <br>
xsa 파일이 있는 경로를 입력한다.

```bash
petalinux-config --get-hw-description ../
```
