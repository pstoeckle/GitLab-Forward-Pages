# gl-pages-forward

The [Technical University of Munich (TUM)](https://www.tum.de/en/) has a nice service for [TinyURLs](https://portal.mytum.de/rds_tinyurl_list).
You can create there short links, e.g., <https://go.tum.de/584374>.
However, you can only do this for `*.tum.de` or `*.lrz.de` addresses.
To circumvent this, I created this repository.
With the Python scripts in here, you can create several *forward* pages, e.g., `index.html` that do nothing else but redirect the browser to a given site.
If you combine these forward pages with the [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/) of the [gitlab.lrz.de](https://gitlab.lrz.de/), you can create a short link for every site you want. 

## Usage

```shell
$ create-forward-pages --help
Usage: create-forward-pages [OPTIONS]

  Creates 'index.html's that forward to a specific URL.

Options:
  -v, --version
  -c, --config-file FILE          [default: config.yml]
  -o, --output DIRECTORY          [default: public]
  -u, --base-url TEXT
  -m, --minify                    If this flag is set, the tool will minify
                                  the HTML.
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```

## Contact

If you have any question, please contact [Patrick Stöckle](mailto:patrick.stoeckle@posteo.de).
