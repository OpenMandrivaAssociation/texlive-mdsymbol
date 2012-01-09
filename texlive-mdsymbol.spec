# revision 25049
# category Package
# catalog-ctan /fonts/mdsymbol
# catalog-date 2012-01-08 14:35:05 +0100
# catalog-license ofl
# catalog-version 0.3
Name:		texlive-mdsymbol
Version:	0.3
Release:	1
Summary:	Symbol fonts to match Adobe Myriad Pro
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/mdsymbol
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mdsymbol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mdsymbol.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a font of mathematical symbols, MyriadPro
The font is designed as a companion to Adobe Myriad Pro, but it
might also fit well with other contemporary typefaces.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/mdsymbol/mdsymbol-a.enc
%{_texmfdistdir}/fonts/enc/dvips/mdsymbol/mdsymbol-b.enc
%{_texmfdistdir}/fonts/enc/dvips/mdsymbol/mdsymbol-c.enc
%{_texmfdistdir}/fonts/enc/dvips/mdsymbol/mdsymbol-d.enc
%{_texmfdistdir}/fonts/enc/dvips/mdsymbol/mdsymbol-e.enc
%{_texmfdistdir}/fonts/enc/dvips/mdsymbol/mdsymbol-f.enc
%{_texmfdistdir}/fonts/map/dvips/mdsymbol/mdsymbol.map
%{_texmfdistdir}/fonts/opentype/public/mdsymbol/MdSymbol-Bold.otf
%{_texmfdistdir}/fonts/opentype/public/mdsymbol/MdSymbol-Light.otf
%{_texmfdistdir}/fonts/opentype/public/mdsymbol/MdSymbol-Regular.otf
%{_texmfdistdir}/fonts/opentype/public/mdsymbol/MdSymbol-Semibold.otf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolA-Bold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolA-Light.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolA-Regular.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolA-Semibold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolA.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolB-Bold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolB-Light.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolB-Regular.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolB-Semibold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolB.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolC-Bold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolC-Light.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolC-Regular.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolC-Semibold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolC.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolD-Bold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolD-Light.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolD-Regular.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolD-Semibold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolD.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolE-Bold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolE-Light.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolE-Regular.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolE-Semibold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolE.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolF-Bold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolF-Light.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolF-Regular.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolF-Semibold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolF.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mdaccents.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mdarrows.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mdbase.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mddelims.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mdgeometric.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mdoperators.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mdrelations.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mdturnstile.mf
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolA-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolA-Light.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolA-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolA-Semibold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolB-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolB-Light.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolB-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolB-Semibold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolC-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolC-Light.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolC-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolC-Semibold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolD-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolD-Light.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolD-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolD-Semibold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolE-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolE-Light.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolE-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolE-Semibold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolF-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolF-Light.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolF-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolF-Semibold.tfm
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolA-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolA-Light.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolA-Regular.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolA-Semibold.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolB-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolB-Light.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolB-Regular.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolB-Semibold.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolC-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolC-Light.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolC-Regular.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolC-Semibold.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolD-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolD-Light.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolD-Regular.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolD-Semibold.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolE-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolE-Light.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolE-Regular.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolE-Semibold.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolF-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolF-Light.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolF-Regular.pfb
%{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolF-Semibold.pfb
%{_texmfdistdir}/tex/latex/mdsymbol/mdsymbol.sty
#- source
%doc %{_texmfdistdir}/source/latex/mdsymbol/mdsymbol.dtx
%doc %{_texmfdistdir}/source/latex/mdsymbol/mdsymbol.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex source %{buildroot}%{_texmfdistdir}
