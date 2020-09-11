import bazel_repositories


URLS = [
    "https://github.com/grpc/grpc/archive/v1.32.0.tar.gz",
    "https://github.com/madler/zlib/archive/v1.2.11.tar.gz",
    "https://github.com/google/jwt_verify_lib/archive/7276a339af8426724b744216f619c99152f8c141.tar.gz",
    "https://mirror.bazel.build/github.com/bazelbuild/bazel-toolchains/archive/2.2.0.tar.gz",
]


def test_deps_names_versions():
    expected = [
        ("bazel-toolchains", "2.2.0",),
        ("grpc", "1.32.0",),
        ("jwt_verify_lib", "7276a339af8426724b744216f619c99152f8c141",),
        ("zlib", "1.2.11",),
    ]

    assert bazel_repositories.deps_names_versions(URLS) == expected


def test_spec_provides():
    expected = ""
    expected += bazel_repositories.AUTOGEN_HEADER
    expected += "Provides:       bundled(bazel-toolchains) = 2.2.0\n"
    expected += "Provides:       bundled(grpc) = 1.32.0\n"
    expected += "Provides:       bundled(jwt_verify_lib) = "
    expected += "7276a339af8426724b744216f619c99152f8c141\n"
    expected += "Provides:       bundled(zlib) = 1.2.11\n"
    expected += bazel_repositories.AUTOGEN_FOOTER

    assert bazel_repositories.spec_provides(URLS) == expected


def test_spec_setup_vendor():
    expected = ""
    expected += bazel_repositories.AUTOGEN_HEADER
    expected += "%setup -q -T -D -a 1\n"
    expected += bazel_repositories.AUTOGEN_FOOTER

    assert bazel_repositories.spec_setup_vendor() == expected
