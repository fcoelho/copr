# https://github.com/mattn/go-localereader
%global goipath         github.com/muesli/ansi
%global commit          c9f0611b6c70fa404402220bebec6d7fcc63741c

%gometa

%global common_description %{expand:
Raw ANSI sequence helpers.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Raw ANSI sequence helpers

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/mattn/go-runewidth)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%check
%gocheck

%gopkgfiles

%changelog
* Thu Oct 13 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com> 0-0.3
- 

* Thu Oct 13 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com> 0-0.1
- new package built with tito

