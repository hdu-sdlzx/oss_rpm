Name: gcc
Version: 14.2.0
Release: 1
Summary: The GNU Compiler Collection
License: GPL-3.0-or-later WITH GCC-exception-3.1
URL: http://gcc.gnu.org

Source0: https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++ make
BuildRequires: gmp-devel mpfr-devel libmpc-devel
# BuildRequires: chrpath
# BuildRequires: isl-devel libzstd-devel

%description
The GNU Compiler Collection includes front ends for C and C++ as well as libraries for C++ (libstdc++)

%prep
%autosetup

%build
# override rpm provided compiler flags
export CFLAGS=""
export CXXFLAGS=""
export LDFLAGS=""

mkdir build
cd build
# libsanitizer has rpath issues:
# 0x0020 an RPATH references '..' of an absolute path; this will break the functionality when the path before '..' is a symlink
# ERROR   0020: file '/usr/lib64/libasan.so.8.0.0' contains a runpath referencing '..' of an absolute path [/usr/lib/../lib64]
# Configure reference:
# https://gcc.gnu.org/install/configure.html
../configure --prefix=%{_prefix} \
	--disable-bootstrap \
	--enable-languages=c,c++ \
	--disable-multilib \
	--disable-libsanitizer \
	--disable-gcov \
	--disable-libquadmath \
	--disable-vtv \
	--disable-libssp \
	--disable-libgomp \
	--disable-lto \
	--with-arch=x86-64-v3
%make_build

%install
cd build
make DESTDIR=%{buildroot} install-strip

%files

%changelog
* Mon Sep 16 2024 Liu Zixian <hdu_sdlzx@163.com> 14.2.0-1
- init
