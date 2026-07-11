%global tl_name mdsymbol
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Symbol fonts to match Adobe Myriad Pro
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/mdsymbol
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mdsymbol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mdsymbol.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mdsymbol.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a font of mathematical symbols, MyriadPro The font
is designed as a companion to Adobe Myriad Pro, but it might also fit
well with other contemporary typefaces.

