# Generated from vagrant_cloud-2.0.1.gem by gem2rpm -*- rpm-spec -*-
%global vagrant_plugin_name vagrant_cloud

Name: vagrant-%{vagrant_plugin_name}
Version: 2.0.2
Release: 1%{?dist}
Summary: Vagrant Cloud API Library
License: MIT
URL: https://github.com/hashicorp/vagrant_cloud
Source0: %{vagrant_plugin_name}-%{version}.gem
# upstream gem doesn't ship tests, pull in from upstream
# git clone https://github.com/hashicorp/vagrant_cloud.git
# cd vagrant_cloud && git checkout v2.0.2
# tar czvf vagrant_cloud-2.0.2-spec.tgz spec
Source1: %{vagrant_plugin_name}-%{version}-spec.tgz
Requires: vagrant
BuildRequires: vagrant
BuildRequires: rubygem(rdoc)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webmock)
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
tar xaf %{SOURCE1}

#sed -i "/^\s*it 'creates a one off box given params' do$/ a skip" \
#  spec/vagrant_cloud/box_spec.rb

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
* Tue Dec 04 2018 Pavel Valena <pvalena@redhat.com> - 2.0.2-1
- Initial package
