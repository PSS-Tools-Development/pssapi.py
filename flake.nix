{
  description = "Wrapper for the Pixel Starships API";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        # Use a system-specific version of Nixpkgs
        pkgs = nixpkgs.legacyPackages.${system};

        # Use Python 3.11
        my-python = pkgs.python311;
      in with pkgs; rec {
        # Development environment (nix develop)
        devShells.default = mkShell {
          name = "poultracker";
          nativeBuildInputs = [ my-python poetry ];
        };
      }
    );
}
