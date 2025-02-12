
from anytree import Resolver, RootResolverError, ChildResolverError


class JunosResolver(Resolver):
    def get(self, node, path):
        node, parts = self._Resolver__start(node, path, self._Resolver__cmp)
        #print(parts)
        not_resolved_indicator = False
        for i in range(0, len(parts)):
            part = parts[i]

            # Attempt to resolve by assuming empty space is not a separator, but part of the node name
            if not_resolved_indicator:
                not_resolved_indicator = False
                # Prepend previous failed attempt at resolving to current item
                part = parts[i-1] + " " + part

            if part == "..":
                parent = node.parent
                if parent is None:
                    raise RootResolverError(node)
                node = parent
            elif part in ("", "."):
                pass
            else:
                try:
                    node = self._Resolver__get(node, part)
                except ChildResolverError as e:
                    # Indicate reference could not be resolved.
                    not_resolved_indicator = True

                    if i == len(parts)-1:
                        raise e

        return node