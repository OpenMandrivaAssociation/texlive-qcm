Name:		texlive-qcm
Version:	63833
Release:	2
Summary:	A LaTeX2e class for making multiple choice questionnaires
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/qcm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qcm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qcm.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qcm.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
QCM is a package for making multiple choices questionnaires
under LaTeX2e ("QCM" is the French acronym for this style of
test). A special environment allows you to define questions and
possible answers. You can specify which answers are correct and
which are not. QCM not only formats the questions for you, but
also generates a 'form' (a grid that your students will have to
fill in), and a 'mask' (the same grid, only with correct
answers properly checked in). You can then print the mask on a
slide and correct the questionnaires more easily by
superimposing the mask on top of students' forms. QCM can also
typeset exam corrections automatically, and comes with support
for AUC-TeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/qcm/qcm.cls
%{_texmfdistdir}/tex/latex/qcm/qcm.sty
%doc %{_texmfdistdir}/doc/latex/qcm/NEWS
%doc %{_texmfdistdir}/doc/latex/qcm/README
%doc %{_texmfdistdir}/doc/latex/qcm/qcm.el
%doc %{_texmfdistdir}/doc/latex/qcm/qcm.pdf
#- source
%doc %{_texmfdistdir}/source/latex/qcm/qcm.dtx
%doc %{_texmfdistdir}/source/latex/qcm/qcm.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
