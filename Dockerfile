FROM fedora:42
RUN sed -e 's|^metalink=|#metalink=|g' -e 's|^#baseurl=http://download.example/pub/fedora/linux|baseurl=https://mirrors.tuna.tsinghua.edu.cn/fedora|g' -i /etc/yum.repos.d/fedora.repo /etc/yum.repos.d/fedora-updates.repo
RUN dnf update -y
RUN dnf install -y rpm-build
