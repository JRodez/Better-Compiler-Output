{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachSystem [ "x86_64-linux" "x86_64-darwin" "aarch64-linux" "aarch64-darwin" ] (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        lib = pkgs.lib;
        python-pkgs = pkgs.python3Packages;
      in  
      {
        packages.default = with python-pkgs; buildPythonApplication  rec  {
          pname = "better-compiler-output";
          version = "0.1.0";
          src = lib.cleanSource ./.;

          propagatedBuildInputs = [
          ];

          buildInputs = [
          ];

          pyproject = true;
          build-system = [ setuptools ];

          meta = with pkgs.lib; {
            description = "A Python project";
            license = licenses.mit;
            platforms = platforms.all;
          };
        };

        devShells.default = pkgs.mkShellNoCC {
          packages = with python-pkgs; [
            ruff
          ];
        };
      }
    );
}
