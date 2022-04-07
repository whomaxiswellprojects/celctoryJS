using System;

namespace Builf {

    class BuildComposerApp {

        private string buildfile, workspace;
        private bool hatched = false;
        private bool debug = false;
        private bool reverse = false;

        public BuildComposerApp(string buildfile, string workspace) {
            this.buildfile = buildfile;
            this.workspace = workspace;
        }

        public BuildComposerApp(string workspace) {
            this.buildfile = "BuildFile";
            this.workspace = workspace;
        } 

        public BuildComposerApp() {
            this.buildfile = "BuildFile";
            this.workspace = workspace;
        }

        public BuildComposerApp(string buildfile) {
            this.buildfile = buildfile;
            this.workspace = ".";
        }

        public void composee() {
        }

        public bool hasHatched() {
            return this.buildfile != null && this.workspace != null && this.hatched;
        }

        public bool hasDebug() {
            return this.buildfile != null && this.workspace != null && this.debug;
        }

        public bool hasReversed() {
            return this.buildfile != null && this.workspace != null && this.reverse;
        }

        public bool setDefine(string defineName, Object value) {
            switch (defineName.ToUpper()) {
                case "DEBUG": {
                    this.debug = (bool) value;
                    break;
                }
                case "HATCH": {
                    this.hatched = (bool) value;
                    break;
                }
                case "REVERSE": {
                    this.reverse = (bool) value;
                    break;
                }
            }
        }
    }

}