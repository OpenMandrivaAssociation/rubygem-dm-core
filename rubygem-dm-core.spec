# Generated from dm-core-1.2.0.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	dm-core

Summary:	An Object/Relational Mapper for Ruby
Name:		rubygem-%{rbname}

Version:	1.2.0
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/datamapper/dm-core
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Faster, Better, Simpler.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/support
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/support/inflector
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/support/ext
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/spec
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/spec/shared
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/spec/shared/public
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/spec/shared/semipublic
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/spec/shared/semipublic/query/conditions
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/spec/shared/semipublic/query
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/spec/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/resource
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/resource/persistence_state
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/query
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/query/conditions
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/model
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/associations
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/core_ext
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/property
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/property/typecast

%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/spec/shared/public/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/spec/shared/semipublic/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/spec/shared/semipublic/query/conditions/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/spec/shared/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/spec/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/query/conditions/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/support/ext/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/support/inflector/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/property/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/property/typecast/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/core_ext/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/associations/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/support/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/spec/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/resource/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/resource/persistence_state/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/query/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/model/*.rb

%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-core/adapters
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-core/adapters/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
