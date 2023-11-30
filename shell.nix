{pkgs ? import <nixpkgs> {}}: let
  pkgs-python = ps:
    with ps; [
      setuptools
      pytest
    ];
  python = pkgs.python311.withPackages pkgs-python;
in
  python.env
