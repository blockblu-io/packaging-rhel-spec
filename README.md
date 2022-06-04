# Cardano RPM packages for Redhat Linux distributions

This repository maintains RPM specification files for a number of Cardano
applications on a number of Redhat Linux releases.

## Software Repository

A number of applications for Cardano ecosystem have been packaged and are
available in our [blockblu.repo](https://repo.blockblu.io). You can install the
repo as following for the given Redhat distributions. Only the distributions
mentioned below are supported. However, the specification files in this Github
repository could be adapted to earlier releases.

**CentOS 7 / CentOS (Almalinux/ Rocky Linux/ Stream) 8**

```bash
curl -s https://repo.blockblu.io/linux/centos/blockblu.repo | \
    sudo tee /etc/yum.repos.d/blockblu.repo
```

**Fedora 35+**

```bash
curl -s https://repo.blockblu.io/linux/fedora/blockblu.repo | \
    sudo tee /etc/yum.repos.d/blockblu.repo
```

## Cardano Applications

### Cardano Node (Haskell implementation of IOG)
The core component that is used to participate in a decentralised Cardano
blockchain (see [code repository](https://github.com/input-output-hk/cardano-node)).
This application can be used to operate a local full node for a Cardano
blockchain, operate a stakepool or a relay.

```bash
sudo yum install cardano-node -y
```

### Cardano CLI
A CLI tool to interact with the `cardano-node` above, which is the core
component that is used to participate in a decentralised Cardano blockchain
(see [code repository](https://github.com/input-output-hk/cardano-node)).

```bash
sudo yum install cardano-cli -y
```

### Cardano Hardware CLI
A Cardano CLI tool for signing transactions with hardware wallets (see
[code repository](https://github.com/vacuumlabs/cardano-hw-cli)). Its
command-line interface is based on the `cardano-cli` tool above. This
application is maintained by [Vacuumlabs](https://vacuumlabs.com).

```bash
sudo yum install cardano-hw-cli -y
```

### CNCLI
A community-based cardano-node CLI tool. It's a collection of utilities to
enhance and extend beyond those available with the cardano-cli (see
[code repository](https://github.com/cardano-community/cncli)). This application
is maintained by community member Andrew Westberg.

```bash
sudo yum install cncli -y
```

## Libraries

### Libsodium
Sodium is a new, easy-to-use software library for encryption, decryption,
signatures, password hashing and more.

It is a portable, cross-compilable, installable, packageable fork of NaCl, with
a compatible API, and an extended API to improve usability even further. Its
goal is to provide all of the core operations needed to build higher-level
cryptographic tools.

IOG (and Algorand team) created a fork of Sodium to implement a draft of
["Verifiable Random Functions"](https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-vrf-03)
(see [code repository](https://github.com/input-output-hk/libsodium)). The
`libsodium` package of our repository provides this fork of IOG.

```bash
sudo yum install libsodium -y
```

The development files of libsodium are included in this package.

```bash
sudo yum install libsodium-devel -y
```

If your system has already a `libsodium` package installed, you have to upgrade
to the `libsodium` package of our repository. It includes the necessary code
from the IOG fork.

```bash
sudo yum upgrade --refresh
```

### Libsecp256k1
Optimized C library for ECDSA signatures and secret/public key operations on
curve secp256k1 (see [code repository](https://github.com/bitcoin-core/secp256k1)).

This library is intended to be the highest quality publicly available library
for cryptography on the secp256k1 curve. However, the primary focus of its
development has been for usage in the Bitcoin system and usage unlike Bitcoin's
may be less well tested, verified, or suffer from a less well thought out
interface. Correct usage requires some care and consideration that the library
is fit for your application's purpose.

```bash
sudo yum install libsecp256k1-cardano -y
```

The development files of `libsecp256k1-cardano` are included in this package.

```bash
sudo yum install libsecp256k1-cardano-devel -y
```

## Feedback

Feel free to open a Github issue on this repository. In particular,

* if you want to see a new Cardano application being packaged
* if you have any issues with a packaged application

### Contacts

* [Kevin Haller](mailto:kevin.haller@blockblu.io) - Operator of [SOBIT](https://staking.outofbits.com) stakepool