Name:		openssl
Version:	4.0.2
Release:	1
Summary:	A toolkit for general-purpose cryptography and secure communication.
License:	Apache-2.0
URL:		https://www.openssl.org/

Source0:	https://github.com/openssl/openssl/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc perl

# replace fedora official packages
Obsoletes:  openssl-libs < 1:%{version}
Obsoletes:  openssl-devel < 1:%{version}
Provides:   openssl-libs = 1:%{version}
Provides:   openssl-libs%{?_isa} = 1:%{version}
Provides:   openssl-devel = 1:%{version}

%description
The OpenSSL software library is a robust, commercial-grade, full-featured toolkit for general-purpose cryptography and secure communication.

%prep
%autosetup

%build
./Configure --prefix=%{_prefix} \
    --openssldir=%{_sysconfdir}/%{name} \
    no-apps no-docs no-tests \
    no-legacy no-deprecated \
    no-comp \
    enable-ktls enable-tfo enable-ec_nistp_64_gcc_128
%make_build

%install
%make_install

%files
%{_includedir}/%{name}
%{_libdir}/libssl.so
%{_libdir}/libssl.so.4
%{_libdir}/libssl.a
%{_libdir}/libcrypto.so
%{_libdir}/libcrypto.so.4
%{_libdir}/libcrypto.a
%{_libdir}/cmake/OpenSSL
%{_libdir}/pkgconfig/openssl.pc
%{_libdir}/pkgconfig/libssl.pc
%{_libdir}/pkgconfig/libcrypto.pc
%{_sysconfdir}/%{name}

%changelog
* Sun Sep 13 2026 Liu Zixian <hdu_sdlzx@163.com> 4.0.2-1
- init
