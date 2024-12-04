{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachSystem [ "x86_64-linux" "x86_64-darwin" "aarch64-linux" "aarch64-darwin" ]
      (system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          lib = pkgs.lib;
          python-pkgs = pkgs.python3Packages;
        in
        {
          packages.default = python-pkgs.buildPythonApplication rec {
            pname = "better-compiler-output";
            version = "0.1.0";
            src = lib.cleanSource ./.;

            propagatedBuildInputs = [
              # python-pkgs.
            ];
            buildInputs = [
              # python-pkgs.
            ];
            meta = with pkgs.lib; {
              description = "A Python project";
              license = licenses.mit;
              platforms = platforms.all;
            };
          };

          devShells.default = pkgs.mkShellNoCC {
            packages = with pkgs; [

            ];
          };
        }
      );
}
