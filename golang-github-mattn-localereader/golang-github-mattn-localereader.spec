# https://github.com/mattn/go-localereader
%global goipath         github.com/mattn/go-localereader
%global commit          2491eb6c1c75720122ef321ed7acc3a8d9de95b1

%gometa

%global common_description %{expand:
CodePage decoder for Windows.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        CodePage decoder for Windows

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/text)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%gopkgfiles

%changelog
* Wed Oct 12 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com> 0-0.6
- 

* Wed Oct 12 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com> 0-0.4
- 

* Wed Oct 12 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com>
- 

* Wed Oct 12 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com> 0-0.3
- 

* Wed Oct 12 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com> 0-0.2
- 

* Wed Oct 12 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com>
- 

* Wed Oct 12 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com>
- 

