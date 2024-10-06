# Uncertainty Classification with Fine-tuned FinBERT

This repository contains the implementation of a fine-tuned model based on Yi Yang's [FinBERT-Pretrained model](https://huggingface.co/yiyanghkust/finbert-pretrain) to perform uncertainty classification on English sentences. The fine-tuned model is trained to classify sentences as either "certain" or "uncertain." 

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Examples](#examples)
- [Model](#model)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

In many financial documents, identifying uncertain statements is crucial for decision-making. This project focuses on fine-tuning the pre-trained FinBERT model to classify sentences based on their uncertainty. The task involves distinguishing between "certain" and "uncertain" sentences, where certain sentences express confidence and uncertain sentences leave room for ambiguity.

### Examples:

**Uncertain sentence:**
> "The company *may* achieve higher revenues next quarter."

**Certain sentence:**
> "The company achieved higher revenues last quarter."

## Dataset

The training data for this project is sourced from the [HUN-REN—SZTE Research Group on Artificial Intelligence](https://rgai.inf.u-szeged.hu/node/160). Specifically, the model has been fine-tuned using annotated data from:

- **FactBank** (Saur and Pustejovsky, 2009)
- **WikiWeasel** (Farkas et al., 2010)

Both of these datasets contain annotations that help identify uncertain language in various contexts. While the original dataset also includes the BioScope corpus (Vincze et al., 2008), we have restricted our focus to **FactBank** and **WikiWeasel** to align with the project's goal of targeting financial domain applications.

## Model

You can access our model at [Huggingface](https://huggingface.co/Zhenyu-Zane/Finbert-Uncertainty). The model is built on top of Yi Yang's [FinBERT-Pretrained model](https://huggingface.co/yiyanghkust/finbert-pretrain), which is specifically optimized for financial tasks. We have further fine-tuned it to classify sentences as either certain or uncertain, using FactBank and WikiWeasel for training.

## Usage

For usage examples, please refer to the [`FinBERT-Uncertainty-demo.py`](./FinBERT-Uncertainty-demo.py) file, which demonstrates how to use the fine-tuned model for uncertainty classification.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue if you find a bug or have a feature request.
