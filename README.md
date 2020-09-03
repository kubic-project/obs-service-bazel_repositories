# obs-service-bazel_repositories
OBS Source Service to download dependencies of projects using Bazel. This allows
offline builds of them on OBS.

It downloads all dependencies which `bazel fetch` would and then it stores them
in the `vendor.tar.gz` archive, which then can be used for offline builds. That
archive contains the complete Bazel cache inside `BAZEL_CACHE` directory, which
means that for a simple project, that archive can be used like:

```
tar -zxf vendor.tar.gz
bazel build \
    --repository_cache=BAZEL_CACHE \
    //...
```

After that, Bazel should build the project without downloading any dependencies.

## Usage for packagers

Let's assume that you are packaging a project called `foobar` and:

- your package is going to be built from `foobar.tar.gz` archive
- it can be built with `bazel build //...` command (which means that the target
  is `//...`)

First of all, before running this service, you need to have a basic `.spec`
file already. For our `foobar` project, it can be as simple as:

```
Name:           foobar
Version:        0.1
Release:        0
Summary:        Simple project using Bazel
License:        Apache-2.0
URL:            https://somegithost.org/foobar/foobar
Source0:        https://somegithost.org/foobar/foobar/archive/v0.1.tar.gz#/foobar-0.1.tar.gz
BuildRequires:  bazel

%prep
%setup -q

%build
bazel build \
    --repository_cache=BAZEL_CACHE \
    //...

%install
install -D -m0755 bazel-bin/foobar %{buildroot}%{_bindir}/foobar

%files
%license LICENSE
%doc README.md
%{_bindir}/foobar

%changelog
```

For that project, create a `_service` file containing:

```
<services>
  <service mode="disabled" name="bazel_repositories">
  </service>
</services>
```

Then run:

```
osc service disabledrun
```

After that, you should have the `vendor.tar.gz` archive and the spec should be
updated with autogeneratd bits which include that archive as a `Source`, list
all included dependencies by it in comments and unpack it with `%setup` macro.

## Demo

[![asciicast](https://asciinema.org/a/358399.svg)](https://asciinema.org/a/358399)

[![asciicast](https://asciinema.org/a/358419.svg)](https://asciinema.org/a/358419)
