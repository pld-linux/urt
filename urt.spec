Summary:	Utah Raster Toolkit
Summary(pl):	Zestaw narz�dzi z Utah do grafiki rastrowej
Name:		urt
Version:	3.1b
Release:	2
License:	GPL-like/"reserved" (see documentation for details)
Group:		Applications/Graphics
Source0:	ftp://ftp.cs.utah.edu/pub/dept/OLD/pub/%{name}-%{version}.tar.Z
Patch0:		%{name}-config.patch
Patch1:		%{name}-fixes.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-shared.patch
BuildRequires:	libtool
BuildRequires:	netpbm-devel
BuildRequires:	libtiff-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Utah Raster toolkit is a collection of programs and C routines for
dealing with raster images commonly encountered in computer graphics.
It provides the following major functions:
 - A device and system independent image format for storing images and
   information about them. Called the RLE format, it uses run length
   encoding to reduce storage space for most images.
 - A library of C routines for reading, writing and manipulating images
   stored in the RLE format.
 - A collections of programs for manipulating and displaying RLE
   images.

%description -l pl
Utah Raster Toolkit to zestaw program�w i funkcji w C do obr�bki
obraz�w rastrowych cz�sto wyst�puj�cych w grafice komputerowej. URT
dostarcza:
 - Niezale�ny od urz�dzenia i systemu format obrazk�w do zapisu grafiki
   i informacji o niej. Nazywa si� RLE i u�ywa kompresji Run-Length
   Encoding, aby zmniejszy� zajmowane miejsce.
 - Zestaw funkcji w C do czytania, pisania i manipulowania obrazkami
   zapisanymi w formacie RLE.
 - Zestaw program�w do manipulowania i wy�wietlania obrazk�w RLE.

%package devel
Summary:	Development files for Utah Raster Toolkit
Summary(pl):	Pakiet dla programist�w Utah Raster Toolkit
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Utah Raster Toolkit header files.

%description devel -l pl
Pliki nag��wkowe Utah Raster Toolkit.

%package static
Summary:	Utah Raster Toolkit static library
Summary(pl):	Statyczna biblioteka Utah Raster Toolkit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	netpbm-rle-static
Provides:	netpbm-rle-static
Conflicts:	netpbm-static < 9.23-2

%description static
Utah Raster Toolkit static library.

%description static -l pl
Statyczna biblioteka Utah Raster Toolkit.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
./Configure
%{__make} ExtraCFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/rle} \
	$RPM_BUILD_ROOT%{_mandir}/man{1,3,5}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf 3.1-changes CHANGES README blurb copyright

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/rle
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_mandir}/man[35]/*

%files static
%defattr(644,root,root,755)
%{_libdir}/librle.a
