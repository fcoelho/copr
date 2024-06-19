Name:           terragrunt
Version:        0.59.4
Release:        1%{?dist}
Summary:        terragrunt

License:        MIT
URL:            https://github.com/gruntwork-io/terragrunt
Source0:        https://github.com/gruntwork-io/terragrunt/archive/v%{version}.tar.gz

BuildRequires: golang
BuildRequires: make
BuildArch: %{_arch}

%description
terragrunt

%prep
%setup -q

%build
make terragrunt

%install
install -D -m 0755 terragrunt %{buildroot}/usr/bin/terragrunt

%files
/usr/bin/terragrunt

%changelog
* Wed Jun 19 2024 Felipe Bessa Coelho <me@fcoelho.pt> 0.59.4-1
- test (me@fcoelho.pt)