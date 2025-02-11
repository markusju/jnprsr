# jnprsr 
jnprsr ('ʤunəpɑrsər) is a **Parser** for **Juniper configuration files**.

It is based around a Lexer and Parser built using **ANTLR4** (https://www.antlr.org/). The formal grammar used in our project was initially created by the **batfish** (https://github.com/batfish/batfish) project.

Our tool allows to generate an **Abstract Syntax Tree (AST)** from a given Juniper configuration file.
This **AST** can then be processed further. Currently, we provide the following functions:

* **Pretty-Printing**
* **Configuration Merge**
* **Sub-Tree Selection**


The **AST** generated by our implementation uses a data-type provided by the **anytree** (https://github.com/c0fec0de/anytree) library. You can easily process the **AST** generated by our implementation and use it in our own tools.

*Please note: This is currently still a **beta release**. This product comes with absolutely no warranty. It is neither supported nor endorsed in any way by Juniper Networks Inc. We assume no liability for any undesired or incorrect behavior you might experience with this software. If you break your network using **jnprsr**, it is your responsibility and you should be ashamed of yourself for not testing your software properly.*

## Installation

You can install jnprsr using pip:
```
pip install jnprsr
```

You can also install directly from Git:
```
pip install git+https://github.com/markusju/jnprsr.git
```
## TL;DR - What you can do with jnprsr

### Pretty-Printing
It allows you to transform a configuration file looking like this

```
interfaces { et-0/0/0 {description "More Bandwidth!"; unit 0 {family inet{address 192.0.2.1/24;}}}}
```

into this

```
interfaces {
    et-0/0/0 {
        description "More Bandwidth!";
        unit 0 {
            family inet {
                address 192.0.2.1/24;
            }
        }
    }
}
```

### Configuration Merge

Suppose you have this snippet
```
interfaces {
    et-0/0/0 {
        description "Skynet NNI";
    }
}
```

and this target configuration
```
interfaces {
    et-0/0/0 {
        unit 0 {
            family inet {
                address 192.0.2.1/24;
            } 
        }
    }
}
```

using **jnprsr** you can perform a `> load merge` operation on the target configuration with the snippet to generate this:

``` 
interfaces {
    et-0/0/0 {
        description "Skynet NNI";
        unit 0 {
            family inet {
                address 192.0.2.1/24;
            } 
        }
    }
}
```


### Sub-Tree Selection

Let's say you have this configuration file:
```
protocols {
    bgp {
        group SKYNET-PEER {
            type external;
            peer-as 1337;
            neighbor 1.2.3.4;
        }
        group EVILCORP-PEER {
            type external;
            peer-as 1338;
            neighbor 1.2.3.5;
        }
        group UMBRELLACORP-PEER {
            type external;
            peer-as 1339;
            neighbor 1.2.3.6;
        }
    }
}
```

and you want to access the sub-tree of the *SKYNET-PEER* BGP peer-group. 

Using **jnprsr** you can easily perform the equivalent of
`> show configuration protocols bgp group SKYNET-PEER`:

```
protocols {
    bgp {
        group SKYNET-PEER {
            type external;
            peer-as 1337;
            neighbor 1.2.3.4;
        }
    }
}
```

### Other Stuff

Since **jnprsr** creates an anytree object, you can easily work with the parsed configuration data. 
Some things you could do include, but are not limited to:

* Validation and/or Verification: Does a certain configuration element or sub-tree exist?
* Comparison: Comparing two given configurations, what nodes are different?
* Editing: Create, Remove, Change a given configuration and generate textual output from the changed tree again.


## Getting Started

### On the shell

**jnprsr** currently comes with 3 commands that you can use on your shell:
- jnprsr-pretty
- jnprsr-subtree
- jnprsr-merge

#### jnprsr-pretty
is a pretty printer. You can supply a Juniper Configuration file and it will [*pretty print*](https://en.wikipedia.org/wiki/Prettyprint) the received configuration. Meaning that the configuration is returned with the proper indentation and spacing.
You can use the script interactively. Simply call it and then paste the configuration. You can end your input on an empty new line with `CTRL+D` or by typing `!END`.

```
$ jnprsr-pretty
[Type CTRL+D or '!END' at a new line to end input]
interfaces { et-0/0/0 {description "More Bandwidth!"; unit 0 {family inet{address 192.0.2.1/24;}}}}
interfaces {
    et-0/0/0 {
        description "More Bandwidth!";
        unit 0 {
            family inet {
                address 192.0.2.1/24;
            }
        }
    }
}
```

Alternatively you can also simply pipe your messed up config at the script to make it pretty. In this case you do not need to end the input.
Note that we are using the `-s` flag in this example. This silences any additional output, so that you can process the output more easily.

```
$ cat what-a-mess.txt | jnprsr-pretty -s
interfaces {
    et-0/0/0 {
        description "More Bandwidth!";
        unit 0 {
            family inet {
                address 192.0.2.1/24;
            }
        }
    }
}
```

#### jnprsr-subtree

is an interactive CLI allowing you to navigate a configuration (almost) as if you are working on a real device.
Once you have loaded the configuration over STDIN you can use the auto completion function using the `<TAB>` key. You can navigate to a suggestion using the arrow keys.

![GIF showing the interactive use of jnprsr-subtree](subtree.gif)
