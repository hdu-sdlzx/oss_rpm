Name:		linux
Version:	6.11.8
Release:	1
Summary:	The Linux kernel
License:	GPL-2.0 WITH Linux-syscall-note
URL:		https://kernel.org/

Source0:	https://cdn.kernel.org/pub/linux/kernel/v6.x/%{name}-%{version}.tar.xz
Source1:	linux.config

BuildRequires:	gcc make flex bison elfutils-devel
BuildRequires:	openssl openssl-devel openssl-devel-engine
BuildRequires:	dwarves

%description
Linux is a clone of the operating system Unix, written from scratch by Linus Torvalds
with assistance from a loosely-knit team of hackers across the Net.
It aims towards POSIX and Single UNIX Specification compliance.

%prep
%autosetup
cp %{SOURCE1} %{_builddir}/%{name}-%{version}/.config

%build
make oldconfig
make -j${RPM_BUILD_NCPUS}

%install
# sudo make INSTALL_MOD_STRIP=1 modules_install
# sudo make install

%files

%changelog
* Mon Nov 18 2024 Liu Zixian <hdu_sdlzx@163.com> 6.11.8-1
- init
