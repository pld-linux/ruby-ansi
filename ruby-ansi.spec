%define	pkgname	ansi
Summary:	ANSI at your fingertips!
Name:		ruby-%{pkgname}
Version:	1.3.0
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	https://github.com/rubyworks/ansi/archive/%{version}.tar.gz
# Source0-md5:	b84f33a9b496c60d855e206d67bdbd74
URL:		http://rubyworks.github.io/ansi/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ANSI project is a superlative collection of ANSI escape code
related libraries enabling ANSI colorization and stylization of
console output. Byte for byte ANSI is the best ANSI code library
available for the Ruby programming language.

%prep
%setup -q -n %{pkgname}-%{version}

# swap symlink to file as we are packaging only lib/*
test -L lib/ansi.yml
mv -f .ruby lib/ansi.yml
ln -s lib/ansi.yml .ruby

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

# wtf is this?
rm $RPM_BUILD_ROOT%{ruby_vendorlibdir}/ansi.rbz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc HISTORY.rdoc NOTICE.rdoc
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
# used by ansi/version.rb to figure out version
%{ruby_vendorlibdir}/%{pkgname}.yml
