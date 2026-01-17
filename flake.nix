{
  description = "Python development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    nixpkgs-python.url = "github:cachix/nixpkgs-python";
  };

  outputs = { self, nixpkgs, nixpkgs-python }: 
    let
      system = "x86_64-linux";

      pythonVersion = "3.12";


      pkgs = import nixpkgs { inherit system; };
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
            # select Python packages here
            matplotlib
            nicegui
            numpy
          ]))
        ];
        shellHook = ''
          python --version
        '';
      };
    };
}
