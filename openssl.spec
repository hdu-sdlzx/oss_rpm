Name:		openssl
Version:	3.5.0
Release:	1
Summary:	A toolkit for general-purpose cryptography and secure communication.
License:	Apache-2.0
URL:		https://www.openssl.org/

Source0:	https://github.com/openssl/openssl/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc perl

# replace fedora official packages
Obsoletes:  openssl-libs < 1:%{version}
Provides:   openssl-libs = 1:%{version}
Provides:   openssl-libs%{?_isa} = 1:%{version}

%description
The OpenSSL software library is a robust, commercial-grade, full-featured toolkit for general-purpose cryptography and secure communication.

%prep
%autosetup

%build
./Configure --prefix=%{_prefix} \
    --openssldir=%{_sysconfdir}/%{name} \
    no-docs no-tests \
    no-legacy no-engine no-deprecated \
    no-apps
# The following configs will break fedora compatibility:
# no-engine: libcurl needs ENGINE_init
# no-deprecated: librpm-sequoia needs RSA_set0_key
%make_build

%install
%make_install

%files
%{_includedir}/%{name}
%{_libdir}/libssl.so
%{_libdir}/libssl.so.3
%{_libdir}/libssl.a
%{_libdir}/libcrypto.so
%{_libdir}/libcrypto.so.3
%{_libdir}/libcrypto.a
%{_libdir}/cmake/OpenSSL
%{_libdir}/pkgconfig/openssl.pc
%{_libdir}/pkgconfig/libssl.pc
%{_libdir}/pkgconfig/libcrypto.pc
%{_sysconfdir}/%{name}

%changelog
* Sun May 04 2025 Liu Zixian <hdu_sdlzx@163.com> 3.5.0-1
- init
