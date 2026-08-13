%global tl_name mdsymbol
%global tl_revision 77682
%global tl_version 0.5

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package provides a font of mathematical symbols, MyriadPro The font
is designed as a companion to Adobe Myriad Pro, but it might also fit
well with other contemporary typefaces.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from mdsymbol:
Map mdsymbol.map
TL_DROPIN_EOF
