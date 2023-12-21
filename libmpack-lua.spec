#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v3
# autospec commit: c1050fe
#
Name     : libmpack-lua
Version  : 1.0.11
Release  : 7
URL      : https://github.com/libmpack/libmpack-lua/archive/1.0.11/libmpack-lua-1.0.11.tar.gz
Source0  : https://github.com/libmpack/libmpack-lua/archive/1.0.11/libmpack-lua-1.0.11.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: libmpack-lua-lib = %{version}-%{release}
Requires: libmpack-lua-license = %{version}-%{release}
BuildRequires : libmpack-dev
BuildRequires : lua-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
## libmpack lua binding
[![Travis Build Status](https://travis-ci.org/libmpack/libmpack-lua.svg?branch=master)](https://travis-ci.org/libmpack/libmpack-lua)

%package lib
Summary: lib components for the libmpack-lua package.
Group: Libraries
Requires: libmpack-lua-license = %{version}-%{release}

%description lib
lib components for the libmpack-lua package.


%package license
Summary: license components for the libmpack-lua package.
Group: Default

%description license
license components for the libmpack-lua package.


%prep
%setup -q -n libmpack-lua-1.0.11
cd %{_builddir}/libmpack-lua-1.0.11
pushd ..
cp -a libmpack-lua-1.0.11 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703191719
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
make  %{?_smp_mflags}  USE_SYSTEM_LUA=yes USE_SYSTEM_MPACK=yes LUA_IMPL=luajit

pushd ../buildavx2
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
make  %{?_smp_mflags}  USE_SYSTEM_LUA=yes USE_SYSTEM_MPACK=yes LUA_IMPL=luajit
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1703191719
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libmpack-lua
cp %{_builddir}/libmpack-lua-%{version}/LICENSE-MIT %{buildroot}/usr/share/package-licenses/libmpack-lua/6a4d33353d2a8e515cb94ba0eac54ec4bfdabb50 || :
pushd ../buildavx2/
%make_install_v3 USE_SYSTEM_LUA=yes USE_SYSTEM_MPACK=yes LUA_IMPL=luajit
popd
%make_install USE_SYSTEM_LUA=yes USE_SYSTEM_MPACK=yes LUA_IMPL=luajit
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/V3/usr/lib/lua/5.1/mpack.so
/usr/lib/lua/5.1/mpack.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmpack-lua/6a4d33353d2a8e515cb94ba0eac54ec4bfdabb50
