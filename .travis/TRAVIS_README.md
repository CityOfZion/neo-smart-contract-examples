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

#### Constant

##### 42

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/constant/forty-two.py test ff 02 False False
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/constant/forty-two.avm ff 02 False False
```

#### Number

##### Add

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/add.py test 0505 02 False False 2 5
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/add.avm 0505 02 False False
```

#### String

##### Character Count

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/string/character-count.py test 07 02 False False lorem
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/string/character-count.avm 07 02 False False
```

#### Array

##### Array Length

``` py
build /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/array/array-length.py test 10 02 False False [True,'two',3]
import contract /Users/lint/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/array/array-length.avm 10 02 False False
```

### From `travis` workstation

#### Number

##### Add

``` py
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/add.py test 0505 02 False False 2 5
import contract /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/number/add.avm 0505 02 False False
```

#### Block

##### Current Height

``` py
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/current-height.py test ff 02 False False
import contract /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/block/current-height.avm ff 02 False False
```

#### Account

##### Is Owner

``` py
build /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/account/is-owner.py test ff 01 False False
import contract /Users/travis/ProjectGit/rockacola/neo-smart-contract-examples/examples/python/account/is-owner.avm ff 01 False False
```

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
