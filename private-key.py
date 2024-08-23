#!/usr/bin/env python3

from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import AtomMainnet
from hdwallet.derivations import BIP44Derivation
from typing import Optional

# Generated previously mnemonic phrase
MNEMONIC: str = 'here should be your twelve of twenty four length mnemonic seed phrase'

# Secret passphrase/password for mnemonic
PASSPHRASE: Optional[str] = None  # "strong-passphrase-password" if you have any

# Initialize Atom mainnet BIP44HDWallet
bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=AtomMainnet)

# Get Atom BIP44HDWallet from mnemonic
bip44_hdwallet.from_mnemonic(
    mnemonic=MNEMONIC, language="english", passphrase=PASSPHRASE
)
# Clean default BIP44 derivation indexes/paths
bip44_hdwallet.clean_derivation()

print("Mnemonic:", bip44_hdwallet.mnemonic())

address_index = 100

# Example of changing account index
"m/44'/-'/0'/0/100"

# Derivation from Atom BIP44 derivation path
bip44_derivation: BIP44Derivation = BIP44Derivation(
    cryptocurrency=AtomMainnet, account=0, change=False, address=address_index
)
# Drive Atom BIP44HDWallet
bip44_hdwallet.from_path(path=bip44_derivation)

# Print address_index, path, address and private_key
print(f"({address_index}) {bip44_hdwallet.path()} {bip44_hdwallet.address()} 0x{bip44_hdwallet.private_key()}")

# Clean derivation indexes/paths
bip44_hdwallet.clean_derivation()
