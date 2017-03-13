%{?scl:%scl_package nodejs-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# needed for building on el6
%{?nodejs_find_provides_and_requires}

%global srcname is-typedarray

Name:           %{?scl_prefix}nodejs-%{srcname}
Version:        1.0.0
Release:        3%{?dist}
Summary:        Detect whether or not an object is a Typed Array
License:        MIT
URL:            https://github.com/hughsk/%{srcname}
Source0:        https://registry.npmjs.org/%{srcname}/-/%{srcname}-%{version}.tgz

BuildArch:      noarch

%if 0%{?rhel} == 6
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch:  %{nodejs_arches} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
#BuildRequires:  %{?scl_prefix}nodejs-tape

%description
%{summary}.

%prep
%autosetup -n package
rm -rf node_modules

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}

cp -pr package.json *.js \
    %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps

#%check
#%nodejs_symlink_deps --check
#%{__nodejs} test.js

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE.md
%{nodejs_sitelib}/%{srcname}

%changelog
* Wed Sep 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-3
- Built for RHSCL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 06 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.0.0-1
- Initial package
