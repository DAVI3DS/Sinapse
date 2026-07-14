#!/usr/bin/env python3
import sys
from src.app import ModpackAnalyzerApp


def main():
    app = ModpackAnalyzerApp(sys.argv)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
