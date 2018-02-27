# Travis README

## Setup

### From `lint` workstation

* Start local docker: `docker start neo-privnet-with-gas`
* Set to project root: `cd /Users/lint/ProjectGit/rockacola/neo-python`
* Check dependencies: `pip3 install -r requirements.txt`
* Start in PrivNet: `python3 prompt.py -p`
* Enable smart contract events: `config sc-events on`
* Open wallet: `open wallet ./demo/wallets/neo-privnet.wallet`
* Rebuild wallet: `wallet rebuild`

---

## Contacts Executions

### From `lint` workstation

#### Constant - 42

* `build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/01-constant/forty-two.py test ff 02 False False`
* `import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/01-constant/forty-two.avm ff 02 False False`

#### Number - Add

* `build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/02-number/add.py test 0505 02 False False 2 5`
* `import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/02-number/add.avm 0505 02 False False`

---

## Developer Notes

### To Do

#### High Priority

* Clean up `functional-utilities`.
* Add examples by split up `UtilContract`.
* Update README with possible examples.
* Once done above, sync to `master`.
* Establish communication to seek for C# dev and Chinese translators.

#### Medium Priority

* Deploy multiple contracts to NEO TestNet

#### Low Priority

* Regression test again NEO TestNet via `neon-js`.

---

## References

TBA
