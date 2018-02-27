# NEO Smart Contract Examples

Collection of well documented examples to get started with smart contract development in NEO blockchain.

## Overview

Check out `/examples` directory for various of example smart contracts in different languages.

### Help Wanted!

This project is urgently seeking for contributors of following categories:

* Smart contract developers to help translate existing Python examples into C#
* Simplified Chinese translator to translate markdown and source documentations

---

## Examples

### Constant

| Name | Description | Python | C#
| --- | --- | --- | ---
| Forty Two | Returns `42`, that's it. | [Source](examples/python/constant/forty-two.py) | N/A
| Local Variable | Returns string value of a local constant. | N/A | N/A
| Global Variable | Returns integer value of a global constant. | N/A | N/A
| Global Variable 2 | Returns bytes value of a global constant. | N/A | N/A

### Number

| Name | Description | Python | C#
| --- | --- | --- | ---
| Add | Sum 2 input numbers together. | [Source](examples/python/number/add.py) | N/A
| Multiply | Multiply 2 input numbers together. | N/A | N/A
| Square | Returns square of an input number. | N/A | N/A
| Power | Base to the exponent power of input numbers. | N/A | N/A
| Fibonacci | Fibonacci value of an input number. | N/A | N/A
| Is Prime | Check if an input number is a prime number. | N/A | N/A

### String

| Name | Description | Python | C#
| --- | --- | --- | ---
| Character Count | Count number of characters of an input string. | [Source](examples/python/string/character-count.py) | N/A
| String Reverse | Provide reverse order of input string. | N/A | N/A

### Array

| Name | Description | Python | C#
| --- | --- | --- | ---
| Array Length | Get item count of an input array. | [Source](examples/python/array/array-length.py) | N/A
| Array Sum | Sum all numbers together from an input number array. | N/A | N/A

### Bytes

TBA

### Storage

TBA

### Block

| Name | Description | Python | C#
| --- | --- | --- | ---
| Current Height | Get current block height. | [Source](examples/python/block/current-height.py) | N/A
| Current Timestamp | Get timestamp of current block. | N/A | N/A
| Block Timestamp | Get timestamp of a given block height. | N/A | N/A
| Block Merkle | Get merkle value of a given block height. | N/A | N/A
| Block Hash | Get hash of a given block height. | N/A | N/A
| Block Consensus | Get consensus value of a given block height. | N/A | N/A
| Next Consensus | Get next consensus value of a given block height. | N/A | N/A

### Account

| Name | Description | Python | C#
| --- | --- | --- | ---
| My Address | Get contract invoker's address. | N/A | N/A
| Target Address | Get contract target's address. | N/A | N/A
| Is Owner | Check if invoker's address matches a static address. | [Source](examples/python/account/is-owner.py) | N/A
| Is Address | Check if invoker's address matches an input address. | N/A | N/A
| Is Address (Witness) | Check if invoker's address matches an input address through `CheckWitness` method. | N/A | N/A

### Validation

TBA

---

## Use Cases

| Name | Description | Python | C#
| --- | --- | --- | ---
| Functional Utilities | TBA | [Source](use-cases/python/functional-utilities/functional-utilities.py) | N/A
| Dictionary | Storage example usage to keep track of stored key value pairs. | N/A | N/A

---

## References

* [Contract Parameter Type Reference](docs/contract-parameter-type.md)

### Resources

* [Python Smart Contract Workshop](https://github.com/CityOfZion/python-smart-contract-workshop)
* [Running a private network of the NEO blockchain](https://medium.com/proof-of-working/how-to-run-a-private-network-of-the-neo-blockchain-d83004557359)

---

## Contribution

`neo-smart-contract-examples` is driven by community code contribution. Before contributing please read the [contributor guidelines](.github/CONTRIBUTING.md) and search the issue tracker as your issue may have already been discussed or fixed. To contribute, fork this project, commit your changes and submit a pull request.

By contributing to this project, you agree that your contributions will be licensed under its MIT license.

---

## License

* Open-source [MIT](LICENSE.md).
* Main author is [@rockacola](https://github.com/rockacola).
