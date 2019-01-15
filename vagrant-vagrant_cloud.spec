# Generated from vagrant_cloud-2.0.1.gem by gem2rpm -*- rpm-spec -*-
%global vagrant_plugin_name vagrant_cloud

Name: vagrant-%{vagrant_plugin_name}
Version: 2.0.1
Release: 1%{?dist}
Summary: Vagrant Cloud API Library
License: MIT
URL: https://github.com/hashicorp/vagrant_cloud
Source0: %{vagrant_plugin_name}-%{version}.gem
Requires: vagrant
BuildRequires: vagrant
BuildRequires: rubygem(rdoc)
BuildRequires: rubygem(rspec)
#BuildRequires: rubygems-devel
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}

%description
Ruby library for the HashiCorp Vagrant Cloud API.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{vagrant_plugin_name}-%{version}

%build
gem build ../%{vagrant_plugin_name}-%{version}.gemspec
%vagrant_plugin_install

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/


%check
pushd .%{vagrant_plugin_instdir}
rspec spec
popd

%files
%dir %{vagrant_plugin_instdir}
%license %{vagrant_plugin_instdir}/LICENSE
%{vagrant_plugin_instdir}/bin
%{vagrant_plugin_libdir}
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%files doc
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/README.md

%changelog
* Tue Dec 04 2018 pvalena <pvalena@redhat.com> - 2.0.1-1
- Initial package
