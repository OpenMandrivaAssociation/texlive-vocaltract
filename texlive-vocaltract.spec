# revision 25629
# category Package
# catalog-ctan /graphics/pstricks/contrib/vocaltract
# catalog-date 2012-03-13 11:09:15 +0100
# catalog-license lppl
# catalog-version 1
Name:		texlive-vocaltract
Version:	1
Release:	1
Summary:	Visualise the vocal tract using LaTeX and PStricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/vocaltract
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vocaltract.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vocaltract.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to visualise the vocal tract. The
vocal tract (in the package) is manipulated by a vector of
articulation parameters according to the S. Maeda model.
Animation may be achieved by providing a sequence of vectors
over time (e.g., from Matlab). A sequence of vectors for
certain German phonemes is embedded in the package, which
allows for animation when no other vector is available. The
package's graphics are produced using pstricks.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/vocaltract/VocalTract.sty
%doc %{_texmfdistdir}/doc/latex/vocaltract/README
%doc %{_texmfdistdir}/doc/latex/vocaltract/vtLatex_AnimationDemo.tex
%doc %{_texmfdistdir}/doc/latex/vocaltract/vtLatex_AnimationLauncher.tex
%doc %{_texmfdistdir}/doc/latex/vocaltract/vtLatex_FigureDemo.pdf
%doc %{_texmfdistdir}/doc/latex/vocaltract/vtLatex_FigureDemo.tex
%doc %{_texmfdistdir}/doc/latex/vocaltract/vtLatex_FigureLauncher.tex
%doc %{_texmfdistdir}/doc/latex/vocaltract/vtLatex_TimeParams.tex
%doc %{_texmfdistdir}/doc/latex/vocaltract/vtMAINVisual.m
%doc %{_texmfdistdir}/doc/latex/vocaltract/vtQueryVisual.m

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1-1
+ Revision: 787818
- Import texlive-vocaltract
- Import texlive-vocaltract

