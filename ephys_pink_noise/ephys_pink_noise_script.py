#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ephys_pink_noise
import logging


def main(args=None):
    ephys_pink_noise.init_log()
    ephys_pink_noise.source_project_configuration('ephys_pink_noise_v1.yml')
    logging.info(f'Starting ephys_pink_noise')


if __name__ == "__main__":
    main()
