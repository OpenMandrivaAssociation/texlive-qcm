%global tl_name qcm
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	A LaTeX2e class for making multiple choice questionnaires
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/qcm
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/qcm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/qcm.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/qcm.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
QCM is a package for making multiple choices questionnaires under
LaTeX2e ("QCM" is the French acronym for this style of test). A special
environment allows you to define questions and possible answers. You can
specify which answers are correct and which are not. QCM not only
formats the questions for you, but also generates a 'form' (a grid that
your students will have to fill in), and a 'mask' (the same grid, only
with correct answers properly checked in). You can then print the mask
on a slide and correct the questionnaires more easily by superimposing
the mask on top of students' forms. QCM can also typeset exam
corrections automatically, and comes with support for AUC-TeX.

