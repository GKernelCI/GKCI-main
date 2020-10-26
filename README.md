# GkernelCI_docker
GkernelCI docker environment

## Quick start

Clone GKernelCI_docker repository  
`git clone --recursive https://github.com/GKernelCI/Gdocker.git`  
Change the *docker-compose.yml* and start docker-compose   
`docker-compose up -d`

## Todo

diagram:
![GKernelCI_V2](https://user-images.githubusercontent.com/107572/91367559-c68eff80-e841-11ea-9e51-2766ba838f2f.png)

- [x] Divide GBuildbot
- [x] Make Gdocker start by `docker-compose up -d`
- [x] Gdocker have tyrian-theme
- [x] Move all the scripts parts to Ghelper
- [ ] Clean old builder configuration
- [ ] Create building factory
- [ ] Make lava testing script from Gbuildbot
- [ ] lava can boot a gentoo testing artifact
- [ ] Creating Gentoo rootfs weekly from buildbot worker
- [ ] lava can boot the created rootfs
- [ ] send email notifications
- [ ] Add lava test other than boot
- [ ] Encrypt secrets with blackbox
- [ ] Create kernel overlay 
- [ ] start to stabilize on kernel overlay
- [ ] send livepatch pull request and commits

## Contribute
Any contribute is welcome

Please check the [issues](https://github.com/GKernelCI/Gdocker/issues) for contributing
