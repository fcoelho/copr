Name:           terragrunt
Version:        0.59.4
Release:        2%{?dist}
Summary:        terragrunt

License:        MIT
URL:            https://github.com/gruntwork-io/terragrunt

%undefine _disable_source_fetch
Source0:        https://github.com/gruntwork-io/terragrunt/archive/v%{version}.tar.gz

BuildRequires: golang
BuildRequires: make
BuildArch: %{_arch}

%description
terragrunt

%prep
%setup

%build
ls -lhaR
make terragrunt

%install
install -D -m 0755 terragrunt %{buildroot}/usr/bin/terragrunt

%files
/usr/bin/terragrunt

%changelog
* Wed Jun 19 2024 Felipe Bessa Coelho <me@fcoelho.pt> 0.59.4-2
- test (me@fcoelho.pt)

* Wed Jun 19 2024 Felipe Bessa Coelho <me@fcoelho.pt> 0.59.4-1
- test (me@fcoelho.pt)
