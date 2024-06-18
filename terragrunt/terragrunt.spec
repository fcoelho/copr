Name:           terragrunt
Version:        0.58.11
Release:        2%{?dist}
Summary:        terragrunt
URL:            https://github.com/gruntwork-io/terragrunt
License:        MIT

Source0:        https://github.com/gruntwork-io/terragrunt/releases/download/v%{version}/terragrunt_linux_amd64

%description
terragrunt

%prep
# No need for prep as we are directly using the downloaded binary

%build
# No need to build anything as we are directly using the downloaded binary

%install
install -D -m 0755 %{SOURCE0} %{buildroot}/usr/bin/terragrunt

%files
/usr/bin/terragrunt
