Name:		curl
Version:	8.22.0
Release:	1
Summary:	command line tool and library for transferring data with URLs
License:	curl
URL:		https://curl.se/

Source0:	https://curl.se/download/%{name}-%{version}.tar.xz

BuildRequires: gcc cmake openssl zlib

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
%cmake \
    -DBUILD_CURL_EXE=OFF \
    -DBUILD_LIBCURL_DOCS=OFF -DBUILD_MISC_DOCS=OFF \
    -DCURL_USE_LIBPSL=OFF \
    -DCURL_ZLIB=ON -DCURL_ZSTD=ON
%cmake_build

%install
%cmake_install

%files
%{_bindir}/curl-config
%{_includedir}/%{name}
%{_libdir}/libcurl.so
%{_libdir}/libcurl.so.4
%{_libdir}/libcurl.so.4.8.0
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/libcurl.pc

%changelog
* Sun Sep 13 2026 Liu Zixian <hdu_sdlzx@163.com> 8.22.0-1
- init
