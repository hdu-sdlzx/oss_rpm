Name:		curl
Version:	8.13.0
Release:	1
Summary:	command line tool and library for transferring data with URLs
License:	curl
URL:		https://curl.se/

Source0:	https://curl.se/download/%{name}-%{version}.tar.xz

BuildRequires: gcc openssl
BuildRequires: autoconf automake libtool

# replace fedora official packages
Obsoletes:  curl < %{version}
Obsoletes:  libcurl < %{version}
Provides:   libcurl = %{version}
Provides:   libcurl%{?_isa} = %{version}

%description
curl is used in command lines or scripts to transfer data.
curl is also libcurl, used in cars, television sets, routers, printers,
audio equipment, mobile phones, tablets, medical devices, settop boxes,
computer games, media players and is the Internet transfer engine for
countless software applications in over twenty billion installations.
curl is used daily by virtually every Internet-using human on the globe.

%prep
%autosetup

%build
autoreconf -fi
mkdir build && cd build
# libpsl is disabled to keep build requirements minimal
# ntlm requires DES3 which is deprecated in openssl
../configure --prefix=%{_prefix} --libdir=%{_libdir} \
    --disable-docs \
    --disable-ntlm \
    --with-openssl \
    --without-libpsl

%make_build

%install
cd build
%make_install

%files
%{_bindir}/curl
%{_bindir}/curl-config
%{_includedir}/%{name}
%{_libdir}/libcurl.so
%{_libdir}/libcurl.so.4
%{_libdir}/libcurl.so.4.8.0
%{_libdir}/libcurl.a
%{_libdir}/pkgconfig/libcurl.pc
%{_datadir}/aclocal/libcurl.m4

%changelog
* Sat May 17 2025 Liu Zixian <hdu_sdlzx@163.com> 8.13.0-1
- init
