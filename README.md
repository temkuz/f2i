# f2i (File to image)

## Description

f2i is a proof of concept cli tool for converting a file into an image and back

## Downloading

```commandline
git clone git@github.com:temkuz/f2i.git
```

## Installation

```commandline
pip install .
```

## Usage

Get help

```commandline
f2i -h
```

Convert file to image
```commandline
f2i convert FILENAME IMAGE_FILENAME 
```

Convert image to file
```commandline
f2i reconvert IMAGE_FILENAME FILENAME
```

Change image resolution
```commandline
f2i convert FILENAME IMAGE_FILENAME -W IMAGE_WIDTH -H IMAGE_HEIGHT
```