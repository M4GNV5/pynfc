r"""Wrapper for nfc-emulation.h

Generated with:
/usr/local/bin/ctypesgen -lnfc libnfc-1.7.1/include/nfc/nfc-emulation.h libnfc-1.7.1/include/nfc/nfc-types.h libnfc-1.7.1/include/nfc/nfc.h libnfc-1.7.1/libnfc/chips/pn53x.h -o pynfc.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python v(3, 2)

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):

    _fields_ = [("raw", POINTER(c_char)), ("data", c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from c_char array
        elif isinstance(obj, c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util


def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []


class LibraryLoader(object):
    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup(object):
        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            try:
                return self.Lookup(path)
            except:
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # then we search the directory where the generated python interface is stored
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, libname):
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir, name)

    def getdirs(self, libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser("~/lib"), "/usr/local/lib", "/usr/lib"]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        if hasattr(sys, "frozen") and sys.frozen == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    class _Directories(dict):
        def __init__(self):
            self.order = 0

        def add(self, directory):
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            o = self.setdefault(directory, self.order)
            if o == self.order:
                self.order += 1

        def extend(self, directories):
            for d in directories:
                self.add(d)

        def ordered(self):
            return (i[0] for i in sorted(self.items(), key=lambda D: D[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive funtion to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as f:
                for D in f:
                    D = D.strip()
                    if not D:
                        continue

                    m = self._include.match(D)
                    if not m:
                        dirs.add(D)
                    else:
                        for D2 in glob.glob(m.group("pattern")):
                            self._get_ld_so_conf_dirs(D2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HPUX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/x86_64-linux-gnu", "/usr/lib/x86_64-linux-gnu"]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        ext_re = re.compile(r"\.s[ol]$")
        for dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for F in other_dirs:
        if not os.path.isabs(F):
            F = os.path.abspath(F)
        load_library.other_dirs.append(F)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["nfc"] = load_library("nfc")

# 1 libraries
# End libraries

# No modules

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/../nfc-internal.h: 175
class struct_nfc_context(Structure):
    pass

nfc_context = struct_nfc_context# /usr/include/nfc/nfc-types.h: 47

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/../nfc-internal.h: 190
class struct_nfc_device(Structure):
    pass

nfc_device = struct_nfc_device# /usr/include/nfc/nfc-types.h: 52

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/../nfc-internal.h: 122
class struct_nfc_driver(Structure):
    pass

nfc_driver = struct_nfc_driver# /usr/include/nfc/nfc-types.h: 57

nfc_connstring = c_char * int(1024)# /usr/include/nfc/nfc-types.h: 62

enum_anon_19 = c_int# /usr/include/nfc/nfc-types.h: 142

NP_TIMEOUT_COMMAND = 0# /usr/include/nfc/nfc-types.h: 142

NP_TIMEOUT_ATR = (NP_TIMEOUT_COMMAND + 1)# /usr/include/nfc/nfc-types.h: 142

NP_TIMEOUT_COM = (NP_TIMEOUT_ATR + 1)# /usr/include/nfc/nfc-types.h: 142

NP_HANDLE_CRC = (NP_TIMEOUT_COM + 1)# /usr/include/nfc/nfc-types.h: 142

NP_HANDLE_PARITY = (NP_HANDLE_CRC + 1)# /usr/include/nfc/nfc-types.h: 142

NP_ACTIVATE_FIELD = (NP_HANDLE_PARITY + 1)# /usr/include/nfc/nfc-types.h: 142

NP_ACTIVATE_CRYPTO1 = (NP_ACTIVATE_FIELD + 1)# /usr/include/nfc/nfc-types.h: 142

NP_INFINITE_SELECT = (NP_ACTIVATE_CRYPTO1 + 1)# /usr/include/nfc/nfc-types.h: 142

NP_ACCEPT_INVALID_FRAMES = (NP_INFINITE_SELECT + 1)# /usr/include/nfc/nfc-types.h: 142

NP_ACCEPT_MULTIPLE_FRAMES = (NP_ACCEPT_INVALID_FRAMES + 1)# /usr/include/nfc/nfc-types.h: 142

NP_AUTO_ISO14443_4 = (NP_ACCEPT_MULTIPLE_FRAMES + 1)# /usr/include/nfc/nfc-types.h: 142

NP_EASY_FRAMING = (NP_AUTO_ISO14443_4 + 1)# /usr/include/nfc/nfc-types.h: 142

NP_FORCE_ISO14443_A = (NP_EASY_FRAMING + 1)# /usr/include/nfc/nfc-types.h: 142

NP_FORCE_ISO14443_B = (NP_FORCE_ISO14443_A + 1)# /usr/include/nfc/nfc-types.h: 142

NP_FORCE_SPEED_106 = (NP_FORCE_ISO14443_B + 1)# /usr/include/nfc/nfc-types.h: 142

nfc_property = enum_anon_19# /usr/include/nfc/nfc-types.h: 142

enum_anon_20 = c_int# /usr/include/nfc/nfc-types.h: 155

NDM_UNDEFINED = 0# /usr/include/nfc/nfc-types.h: 155

NDM_PASSIVE = (NDM_UNDEFINED + 1)# /usr/include/nfc/nfc-types.h: 155

NDM_ACTIVE = (NDM_PASSIVE + 1)# /usr/include/nfc/nfc-types.h: 155

nfc_dep_mode = enum_anon_20# /usr/include/nfc/nfc-types.h: 155

# /usr/include/nfc/nfc-types.h: 179
class struct_anon_21(Structure):
    pass

struct_anon_21._pack_ = 1
struct_anon_21.__slots__ = [
    'abtNFCID3',
    'btDID',
    'btBS',
    'btBR',
    'btTO',
    'btPP',
    'abtGB',
    'szGB',
    'ndm',
]
struct_anon_21._fields_ = [
    ('abtNFCID3', c_uint8 * int(10)),
    ('btDID', c_uint8),
    ('btBS', c_uint8),
    ('btBR', c_uint8),
    ('btTO', c_uint8),
    ('btPP', c_uint8),
    ('abtGB', c_uint8 * int(48)),
    ('szGB', c_size_t),
    ('ndm', nfc_dep_mode),
]

nfc_dep_info = struct_anon_21# /usr/include/nfc/nfc-types.h: 179

# /usr/include/nfc/nfc-types.h: 192
class struct_anon_22(Structure):
    pass

struct_anon_22._pack_ = 1
struct_anon_22.__slots__ = [
    'abtAtqa',
    'btSak',
    'szUidLen',
    'abtUid',
    'szAtsLen',
    'abtAts',
]
struct_anon_22._fields_ = [
    ('abtAtqa', c_uint8 * int(2)),
    ('btSak', c_uint8),
    ('szUidLen', c_size_t),
    ('abtUid', c_uint8 * int(10)),
    ('szAtsLen', c_size_t),
    ('abtAts', c_uint8 * int(254)),
]

nfc_iso14443a_info = struct_anon_22# /usr/include/nfc/nfc-types.h: 192

# /usr/include/nfc/nfc-types.h: 204
class struct_anon_23(Structure):
    pass

struct_anon_23._pack_ = 1
struct_anon_23.__slots__ = [
    'szLen',
    'btResCode',
    'abtId',
    'abtPad',
    'abtSysCode',
]
struct_anon_23._fields_ = [
    ('szLen', c_size_t),
    ('btResCode', c_uint8),
    ('abtId', c_uint8 * int(8)),
    ('abtPad', c_uint8 * int(8)),
    ('abtSysCode', c_uint8 * int(2)),
]

nfc_felica_info = struct_anon_23# /usr/include/nfc/nfc-types.h: 204

# /usr/include/nfc/nfc-types.h: 219
class struct_anon_24(Structure):
    pass

struct_anon_24._pack_ = 1
struct_anon_24.__slots__ = [
    'abtPupi',
    'abtApplicationData',
    'abtProtocolInfo',
    'ui8CardIdentifier',
]
struct_anon_24._fields_ = [
    ('abtPupi', c_uint8 * int(4)),
    ('abtApplicationData', c_uint8 * int(4)),
    ('abtProtocolInfo', c_uint8 * int(3)),
    ('ui8CardIdentifier', c_uint8),
]

nfc_iso14443b_info = struct_anon_24# /usr/include/nfc/nfc-types.h: 219

# /usr/include/nfc/nfc-types.h: 235
class struct_anon_25(Structure):
    pass

struct_anon_25._pack_ = 1
struct_anon_25.__slots__ = [
    'abtDIV',
    'btVerLog',
    'btConfig',
    'szAtrLen',
    'abtAtr',
]
struct_anon_25._fields_ = [
    ('abtDIV', c_uint8 * int(4)),
    ('btVerLog', c_uint8),
    ('btConfig', c_uint8),
    ('szAtrLen', c_size_t),
    ('abtAtr', c_uint8 * int(33)),
]

nfc_iso14443bi_info = struct_anon_25# /usr/include/nfc/nfc-types.h: 235

# /usr/include/nfc/nfc-types.h: 243
class struct_anon_26(Structure):
    pass

struct_anon_26._pack_ = 1
struct_anon_26.__slots__ = [
    'abtUID',
]
struct_anon_26._fields_ = [
    ('abtUID', c_uint8 * int(8)),
]

nfc_iso14443b2sr_info = struct_anon_26# /usr/include/nfc/nfc-types.h: 243

# /usr/include/nfc/nfc-types.h: 253
class struct_anon_27(Structure):
    pass

struct_anon_27._pack_ = 1
struct_anon_27.__slots__ = [
    'abtUID',
    'btProdCode',
    'btFabCode',
]
struct_anon_27._fields_ = [
    ('abtUID', c_uint8 * int(4)),
    ('btProdCode', c_uint8),
    ('btFabCode', c_uint8),
]

nfc_iso14443b2ct_info = struct_anon_27# /usr/include/nfc/nfc-types.h: 253

# /usr/include/nfc/nfc-types.h: 262
class struct_anon_28(Structure):
    pass

struct_anon_28._pack_ = 1
struct_anon_28.__slots__ = [
    'btSensRes',
    'btId',
]
struct_anon_28._fields_ = [
    ('btSensRes', c_uint8 * int(2)),
    ('btId', c_uint8 * int(4)),
]

nfc_jewel_info = struct_anon_28# /usr/include/nfc/nfc-types.h: 262

# /usr/include/nfc/nfc-types.h: 277
class union_anon_29(Union):
    pass

union_anon_29._pack_ = 1
union_anon_29.__slots__ = [
    'nai',
    'nfi',
    'nbi',
    'nii',
    'nsi',
    'nci',
    'nji',
    'ndi',
]
union_anon_29._fields_ = [
    ('nai', nfc_iso14443a_info),
    ('nfi', nfc_felica_info),
    ('nbi', nfc_iso14443b_info),
    ('nii', nfc_iso14443bi_info),
    ('nsi', nfc_iso14443b2sr_info),
    ('nci', nfc_iso14443b2ct_info),
    ('nji', nfc_jewel_info),
    ('ndi', nfc_dep_info),
]

nfc_target_info = union_anon_29# /usr/include/nfc/nfc-types.h: 277

enum_anon_30 = c_int# /usr/include/nfc/nfc-types.h: 289

NBR_UNDEFINED = 0# /usr/include/nfc/nfc-types.h: 289

NBR_106 = (NBR_UNDEFINED + 1)# /usr/include/nfc/nfc-types.h: 289

NBR_212 = (NBR_106 + 1)# /usr/include/nfc/nfc-types.h: 289

NBR_424 = (NBR_212 + 1)# /usr/include/nfc/nfc-types.h: 289

NBR_847 = (NBR_424 + 1)# /usr/include/nfc/nfc-types.h: 289

nfc_baud_rate = enum_anon_30# /usr/include/nfc/nfc-types.h: 289

enum_anon_31 = c_int# /usr/include/nfc/nfc-types.h: 304

NMT_ISO14443A = 1# /usr/include/nfc/nfc-types.h: 304

NMT_JEWEL = (NMT_ISO14443A + 1)# /usr/include/nfc/nfc-types.h: 304

NMT_ISO14443B = (NMT_JEWEL + 1)# /usr/include/nfc/nfc-types.h: 304

NMT_ISO14443BI = (NMT_ISO14443B + 1)# /usr/include/nfc/nfc-types.h: 304

NMT_ISO14443B2SR = (NMT_ISO14443BI + 1)# /usr/include/nfc/nfc-types.h: 304

NMT_ISO14443B2CT = (NMT_ISO14443B2SR + 1)# /usr/include/nfc/nfc-types.h: 304

NMT_FELICA = (NMT_ISO14443B2CT + 1)# /usr/include/nfc/nfc-types.h: 304

NMT_DEP = (NMT_FELICA + 1)# /usr/include/nfc/nfc-types.h: 304

nfc_modulation_type = enum_anon_31# /usr/include/nfc/nfc-types.h: 304

enum_anon_32 = c_int# /usr/include/nfc/nfc-types.h: 313

N_TARGET = 0# /usr/include/nfc/nfc-types.h: 313

N_INITIATOR = (N_TARGET + 1)# /usr/include/nfc/nfc-types.h: 313

nfc_mode = enum_anon_32# /usr/include/nfc/nfc-types.h: 313

# /usr/include/nfc/nfc-types.h: 322
class struct_anon_33(Structure):
    pass

struct_anon_33._pack_ = 1
struct_anon_33.__slots__ = [
    'nmt',
    'nbr',
]
struct_anon_33._fields_ = [
    ('nmt', nfc_modulation_type),
    ('nbr', nfc_baud_rate),
]

nfc_modulation = struct_anon_33# /usr/include/nfc/nfc-types.h: 322

# /usr/include/nfc/nfc-types.h: 331
class struct_anon_34(Structure):
    pass

struct_anon_34._pack_ = 1
struct_anon_34.__slots__ = [
    'nti',
    'nm',
]
struct_anon_34._fields_ = [
    ('nti', nfc_target_info),
    ('nm', nfc_modulation),
]

nfc_target = struct_anon_34# /usr/include/nfc/nfc-types.h: 331

# /usr/include/nfc/nfc.h: 86
if _libs["nfc"].has("nfc_init", "cdecl"):
    nfc_init = _libs["nfc"].get("nfc_init", "cdecl")
    nfc_init.argtypes = [POINTER(POINTER(nfc_context))]
    nfc_init.restype = None

# /usr/include/nfc/nfc.h: 87
if _libs["nfc"].has("nfc_exit", "cdecl"):
    nfc_exit = _libs["nfc"].get("nfc_exit", "cdecl")
    nfc_exit.argtypes = [POINTER(nfc_context)]
    nfc_exit.restype = None

# /usr/include/nfc/nfc.h: 88
if _libs["nfc"].has("nfc_register_driver", "cdecl"):
    nfc_register_driver = _libs["nfc"].get("nfc_register_driver", "cdecl")
    nfc_register_driver.argtypes = [POINTER(nfc_driver)]
    nfc_register_driver.restype = c_int

# /usr/include/nfc/nfc.h: 91
if _libs["nfc"].has("nfc_open", "cdecl"):
    nfc_open = _libs["nfc"].get("nfc_open", "cdecl")
    nfc_open.argtypes = [POINTER(nfc_context), nfc_connstring]
    nfc_open.restype = POINTER(nfc_device)

# /usr/include/nfc/nfc.h: 92
if _libs["nfc"].has("nfc_close", "cdecl"):
    nfc_close = _libs["nfc"].get("nfc_close", "cdecl")
    nfc_close.argtypes = [POINTER(nfc_device)]
    nfc_close.restype = None

# /usr/include/nfc/nfc.h: 93
if _libs["nfc"].has("nfc_abort_command", "cdecl"):
    nfc_abort_command = _libs["nfc"].get("nfc_abort_command", "cdecl")
    nfc_abort_command.argtypes = [POINTER(nfc_device)]
    nfc_abort_command.restype = c_int

# /usr/include/nfc/nfc.h: 94
if _libs["nfc"].has("nfc_list_devices", "cdecl"):
    nfc_list_devices = _libs["nfc"].get("nfc_list_devices", "cdecl")
    nfc_list_devices.argtypes = [POINTER(nfc_context), POINTER(nfc_connstring), c_size_t]
    nfc_list_devices.restype = c_size_t

# /usr/include/nfc/nfc.h: 95
if _libs["nfc"].has("nfc_idle", "cdecl"):
    nfc_idle = _libs["nfc"].get("nfc_idle", "cdecl")
    nfc_idle.argtypes = [POINTER(nfc_device)]
    nfc_idle.restype = c_int

# /usr/include/nfc/nfc.h: 98
if _libs["nfc"].has("nfc_initiator_init", "cdecl"):
    nfc_initiator_init = _libs["nfc"].get("nfc_initiator_init", "cdecl")
    nfc_initiator_init.argtypes = [POINTER(nfc_device)]
    nfc_initiator_init.restype = c_int

# /usr/include/nfc/nfc.h: 99
if _libs["nfc"].has("nfc_initiator_init_secure_element", "cdecl"):
    nfc_initiator_init_secure_element = _libs["nfc"].get("nfc_initiator_init_secure_element", "cdecl")
    nfc_initiator_init_secure_element.argtypes = [POINTER(nfc_device)]
    nfc_initiator_init_secure_element.restype = c_int

# /usr/include/nfc/nfc.h: 100
if _libs["nfc"].has("nfc_initiator_select_passive_target", "cdecl"):
    nfc_initiator_select_passive_target = _libs["nfc"].get("nfc_initiator_select_passive_target", "cdecl")
    nfc_initiator_select_passive_target.argtypes = [POINTER(nfc_device), nfc_modulation, POINTER(c_uint8), c_size_t, POINTER(nfc_target)]
    nfc_initiator_select_passive_target.restype = c_int

# /usr/include/nfc/nfc.h: 101
if _libs["nfc"].has("nfc_initiator_list_passive_targets", "cdecl"):
    nfc_initiator_list_passive_targets = _libs["nfc"].get("nfc_initiator_list_passive_targets", "cdecl")
    nfc_initiator_list_passive_targets.argtypes = [POINTER(nfc_device), nfc_modulation, POINTER(nfc_target), c_size_t]
    nfc_initiator_list_passive_targets.restype = c_int

# /usr/include/nfc/nfc.h: 102
if _libs["nfc"].has("nfc_initiator_poll_target", "cdecl"):
    nfc_initiator_poll_target = _libs["nfc"].get("nfc_initiator_poll_target", "cdecl")
    nfc_initiator_poll_target.argtypes = [POINTER(nfc_device), POINTER(nfc_modulation), c_size_t, c_uint8, c_uint8, POINTER(nfc_target)]
    nfc_initiator_poll_target.restype = c_int

# /usr/include/nfc/nfc.h: 103
if _libs["nfc"].has("nfc_initiator_select_dep_target", "cdecl"):
    nfc_initiator_select_dep_target = _libs["nfc"].get("nfc_initiator_select_dep_target", "cdecl")
    nfc_initiator_select_dep_target.argtypes = [POINTER(nfc_device), nfc_dep_mode, nfc_baud_rate, POINTER(nfc_dep_info), POINTER(nfc_target), c_int]
    nfc_initiator_select_dep_target.restype = c_int

# /usr/include/nfc/nfc.h: 104
if _libs["nfc"].has("nfc_initiator_poll_dep_target", "cdecl"):
    nfc_initiator_poll_dep_target = _libs["nfc"].get("nfc_initiator_poll_dep_target", "cdecl")
    nfc_initiator_poll_dep_target.argtypes = [POINTER(nfc_device), nfc_dep_mode, nfc_baud_rate, POINTER(nfc_dep_info), POINTER(nfc_target), c_int]
    nfc_initiator_poll_dep_target.restype = c_int

# /usr/include/nfc/nfc.h: 105
if _libs["nfc"].has("nfc_initiator_deselect_target", "cdecl"):
    nfc_initiator_deselect_target = _libs["nfc"].get("nfc_initiator_deselect_target", "cdecl")
    nfc_initiator_deselect_target.argtypes = [POINTER(nfc_device)]
    nfc_initiator_deselect_target.restype = c_int

# /usr/include/nfc/nfc.h: 106
if _libs["nfc"].has("nfc_initiator_transceive_bytes", "cdecl"):
    nfc_initiator_transceive_bytes = _libs["nfc"].get("nfc_initiator_transceive_bytes", "cdecl")
    nfc_initiator_transceive_bytes.argtypes = [POINTER(nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8), c_size_t, c_int]
    nfc_initiator_transceive_bytes.restype = c_int

# /usr/include/nfc/nfc.h: 107
if _libs["nfc"].has("nfc_initiator_transceive_bits", "cdecl"):
    nfc_initiator_transceive_bits = _libs["nfc"].get("nfc_initiator_transceive_bits", "cdecl")
    nfc_initiator_transceive_bits.argtypes = [POINTER(nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_uint8), c_size_t, POINTER(c_uint8)]
    nfc_initiator_transceive_bits.restype = c_int

# /usr/include/nfc/nfc.h: 108
if _libs["nfc"].has("nfc_initiator_transceive_bytes_timed", "cdecl"):
    nfc_initiator_transceive_bytes_timed = _libs["nfc"].get("nfc_initiator_transceive_bytes_timed", "cdecl")
    nfc_initiator_transceive_bytes_timed.argtypes = [POINTER(nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8), c_size_t, POINTER(c_uint32)]
    nfc_initiator_transceive_bytes_timed.restype = c_int

# /usr/include/nfc/nfc.h: 109
if _libs["nfc"].has("nfc_initiator_transceive_bits_timed", "cdecl"):
    nfc_initiator_transceive_bits_timed = _libs["nfc"].get("nfc_initiator_transceive_bits_timed", "cdecl")
    nfc_initiator_transceive_bits_timed.argtypes = [POINTER(nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_uint32)]
    nfc_initiator_transceive_bits_timed.restype = c_int

# /usr/include/nfc/nfc.h: 110
if _libs["nfc"].has("nfc_initiator_target_is_present", "cdecl"):
    nfc_initiator_target_is_present = _libs["nfc"].get("nfc_initiator_target_is_present", "cdecl")
    nfc_initiator_target_is_present.argtypes = [POINTER(nfc_device), POINTER(nfc_target)]
    nfc_initiator_target_is_present.restype = c_int

# /usr/include/nfc/nfc.h: 113
if _libs["nfc"].has("nfc_target_init", "cdecl"):
    nfc_target_init = _libs["nfc"].get("nfc_target_init", "cdecl")
    nfc_target_init.argtypes = [POINTER(nfc_device), POINTER(nfc_target), POINTER(c_uint8), c_size_t, c_int]
    nfc_target_init.restype = c_int

# /usr/include/nfc/nfc.h: 114
if _libs["nfc"].has("nfc_target_send_bytes", "cdecl"):
    nfc_target_send_bytes = _libs["nfc"].get("nfc_target_send_bytes", "cdecl")
    nfc_target_send_bytes.argtypes = [POINTER(nfc_device), POINTER(c_uint8), c_size_t, c_int]
    nfc_target_send_bytes.restype = c_int

# /usr/include/nfc/nfc.h: 115
if _libs["nfc"].has("nfc_target_receive_bytes", "cdecl"):
    nfc_target_receive_bytes = _libs["nfc"].get("nfc_target_receive_bytes", "cdecl")
    nfc_target_receive_bytes.argtypes = [POINTER(nfc_device), POINTER(c_uint8), c_size_t, c_int]
    nfc_target_receive_bytes.restype = c_int

# /usr/include/nfc/nfc.h: 116
if _libs["nfc"].has("nfc_target_send_bits", "cdecl"):
    nfc_target_send_bits = _libs["nfc"].get("nfc_target_send_bits", "cdecl")
    nfc_target_send_bits.argtypes = [POINTER(nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8)]
    nfc_target_send_bits.restype = c_int

# /usr/include/nfc/nfc.h: 117
if _libs["nfc"].has("nfc_target_receive_bits", "cdecl"):
    nfc_target_receive_bits = _libs["nfc"].get("nfc_target_receive_bits", "cdecl")
    nfc_target_receive_bits.argtypes = [POINTER(nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8)]
    nfc_target_receive_bits.restype = c_int

# /usr/include/nfc/nfc.h: 120
if _libs["nfc"].has("nfc_strerror", "cdecl"):
    nfc_strerror = _libs["nfc"].get("nfc_strerror", "cdecl")
    nfc_strerror.argtypes = [POINTER(nfc_device)]
    nfc_strerror.restype = c_char_p

# /usr/include/nfc/nfc.h: 121
if _libs["nfc"].has("nfc_strerror_r", "cdecl"):
    nfc_strerror_r = _libs["nfc"].get("nfc_strerror_r", "cdecl")
    nfc_strerror_r.argtypes = [POINTER(nfc_device), String, c_size_t]
    nfc_strerror_r.restype = c_int

# /usr/include/nfc/nfc.h: 122
if _libs["nfc"].has("nfc_perror", "cdecl"):
    nfc_perror = _libs["nfc"].get("nfc_perror", "cdecl")
    nfc_perror.argtypes = [POINTER(nfc_device), String]
    nfc_perror.restype = None

# /usr/include/nfc/nfc.h: 123
if _libs["nfc"].has("nfc_device_get_last_error", "cdecl"):
    nfc_device_get_last_error = _libs["nfc"].get("nfc_device_get_last_error", "cdecl")
    nfc_device_get_last_error.argtypes = [POINTER(nfc_device)]
    nfc_device_get_last_error.restype = c_int

# /usr/include/nfc/nfc.h: 126
if _libs["nfc"].has("nfc_device_get_name", "cdecl"):
    nfc_device_get_name = _libs["nfc"].get("nfc_device_get_name", "cdecl")
    nfc_device_get_name.argtypes = [POINTER(nfc_device)]
    nfc_device_get_name.restype = c_char_p

# /usr/include/nfc/nfc.h: 127
if _libs["nfc"].has("nfc_device_get_connstring", "cdecl"):
    nfc_device_get_connstring = _libs["nfc"].get("nfc_device_get_connstring", "cdecl")
    nfc_device_get_connstring.argtypes = [POINTER(nfc_device)]
    nfc_device_get_connstring.restype = c_char_p

# /usr/include/nfc/nfc.h: 128
if _libs["nfc"].has("nfc_device_get_supported_modulation", "cdecl"):
    nfc_device_get_supported_modulation = _libs["nfc"].get("nfc_device_get_supported_modulation", "cdecl")
    nfc_device_get_supported_modulation.argtypes = [POINTER(nfc_device), nfc_mode, POINTER(POINTER(nfc_modulation_type))]
    nfc_device_get_supported_modulation.restype = c_int

# /usr/include/nfc/nfc.h: 129
if _libs["nfc"].has("nfc_device_get_supported_baud_rate", "cdecl"):
    nfc_device_get_supported_baud_rate = _libs["nfc"].get("nfc_device_get_supported_baud_rate", "cdecl")
    nfc_device_get_supported_baud_rate.argtypes = [POINTER(nfc_device), nfc_modulation_type, POINTER(POINTER(nfc_baud_rate))]
    nfc_device_get_supported_baud_rate.restype = c_int

# /usr/include/nfc/nfc.h: 132
if _libs["nfc"].has("nfc_device_set_property_int", "cdecl"):
    nfc_device_set_property_int = _libs["nfc"].get("nfc_device_set_property_int", "cdecl")
    nfc_device_set_property_int.argtypes = [POINTER(nfc_device), nfc_property, c_int]
    nfc_device_set_property_int.restype = c_int

# /usr/include/nfc/nfc.h: 133
if _libs["nfc"].has("nfc_device_set_property_bool", "cdecl"):
    nfc_device_set_property_bool = _libs["nfc"].get("nfc_device_set_property_bool", "cdecl")
    nfc_device_set_property_bool.argtypes = [POINTER(nfc_device), nfc_property, c_bool]
    nfc_device_set_property_bool.restype = c_int

# /usr/include/nfc/nfc.h: 136
if _libs["nfc"].has("iso14443a_crc", "cdecl"):
    iso14443a_crc = _libs["nfc"].get("iso14443a_crc", "cdecl")
    iso14443a_crc.argtypes = [POINTER(c_uint8), c_size_t, POINTER(c_uint8)]
    iso14443a_crc.restype = None

# /usr/include/nfc/nfc.h: 137
if _libs["nfc"].has("iso14443a_crc_append", "cdecl"):
    iso14443a_crc_append = _libs["nfc"].get("iso14443a_crc_append", "cdecl")
    iso14443a_crc_append.argtypes = [POINTER(c_uint8), c_size_t]
    iso14443a_crc_append.restype = None

# /usr/include/nfc/nfc.h: 138
for _lib in _libs.values():
    if not _lib.has("iso14443b_crc", "cdecl"):
        continue
    iso14443b_crc = _lib.get("iso14443b_crc", "cdecl")
    iso14443b_crc.argtypes = [POINTER(c_uint8), c_size_t, POINTER(c_uint8)]
    iso14443b_crc.restype = None
    break

# /usr/include/nfc/nfc.h: 139
for _lib in _libs.values():
    if not _lib.has("iso14443b_crc_append", "cdecl"):
        continue
    iso14443b_crc_append = _lib.get("iso14443b_crc_append", "cdecl")
    iso14443b_crc_append.argtypes = [POINTER(c_uint8), c_size_t]
    iso14443b_crc_append.restype = None
    break

# /usr/include/nfc/nfc.h: 140
if _libs["nfc"].has("iso14443a_locate_historical_bytes", "cdecl"):
    iso14443a_locate_historical_bytes = _libs["nfc"].get("iso14443a_locate_historical_bytes", "cdecl")
    iso14443a_locate_historical_bytes.argtypes = [POINTER(c_uint8), c_size_t, POINTER(c_size_t)]
    iso14443a_locate_historical_bytes.restype = POINTER(c_uint8)

# /usr/include/nfc/nfc.h: 142
if _libs["nfc"].has("nfc_free", "cdecl"):
    nfc_free = _libs["nfc"].get("nfc_free", "cdecl")
    nfc_free.argtypes = [POINTER(None)]
    nfc_free.restype = None

# /usr/include/nfc/nfc.h: 143
if _libs["nfc"].has("nfc_version", "cdecl"):
    nfc_version = _libs["nfc"].get("nfc_version", "cdecl")
    nfc_version.argtypes = []
    nfc_version.restype = c_char_p

# /usr/include/nfc/nfc.h: 144
if _libs["nfc"].has("nfc_device_get_information_about", "cdecl"):
    nfc_device_get_information_about = _libs["nfc"].get("nfc_device_get_information_about", "cdecl")
    nfc_device_get_information_about.argtypes = [POINTER(nfc_device), POINTER(POINTER(c_char))]
    nfc_device_get_information_about.restype = c_int

# /usr/include/nfc/nfc.h: 147
if _libs["nfc"].has("str_nfc_modulation_type", "cdecl"):
    str_nfc_modulation_type = _libs["nfc"].get("str_nfc_modulation_type", "cdecl")
    str_nfc_modulation_type.argtypes = [nfc_modulation_type]
    str_nfc_modulation_type.restype = c_char_p

# /usr/include/nfc/nfc.h: 148
if _libs["nfc"].has("str_nfc_baud_rate", "cdecl"):
    str_nfc_baud_rate = _libs["nfc"].get("str_nfc_baud_rate", "cdecl")
    str_nfc_baud_rate.argtypes = [nfc_baud_rate]
    str_nfc_baud_rate.restype = c_char_p

# /usr/include/nfc/nfc.h: 149
if _libs["nfc"].has("str_nfc_target", "cdecl"):
    str_nfc_target = _libs["nfc"].get("str_nfc_target", "cdecl")
    str_nfc_target.argtypes = [POINTER(POINTER(c_char)), POINTER(nfc_target), c_bool]
    str_nfc_target.restype = c_int

# /home/jakob/git/pynfc/libnfc-1.7.1/include/nfc/nfc-emulation.h: 49
class struct_nfc_emulator(Structure):
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/include/nfc/nfc-emulation.h: 59
class struct_nfc_emulation_state_machine(Structure):
    pass

struct_nfc_emulator.__slots__ = [
    'target',
    'state_machine',
    'user_data',
]
struct_nfc_emulator._fields_ = [
    ('target', POINTER(nfc_target)),
    ('state_machine', POINTER(struct_nfc_emulation_state_machine)),
    ('user_data', POINTER(None)),
]

struct_nfc_emulation_state_machine.__slots__ = [
    'io',
    'data',
]
struct_nfc_emulation_state_machine._fields_ = [
    ('io', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_emulator), POINTER(c_uint8), c_size_t, POINTER(c_uint8), c_size_t)),
    ('data', POINTER(None)),
]

# /home/jakob/git/pynfc/libnfc-1.7.1/include/nfc/nfc-emulation.h: 64
if _libs["nfc"].has("nfc_emulate_target", "cdecl"):
    nfc_emulate_target = _libs["nfc"].get("nfc_emulate_target", "cdecl")
    nfc_emulate_target.argtypes = [POINTER(nfc_device), POINTER(struct_nfc_emulator), c_int]
    nfc_emulate_target.restype = c_int

enum_anon_35 = c_int# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/../nfc-internal.h: 120

scan_type_enum = enum_anon_35# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/../nfc-internal.h: 120

struct_nfc_driver.__slots__ = [
    'name',
    'scan_type',
    'scan',
    'open',
    'close',
    'strerror',
    'initiator_init',
    'initiator_init_secure_element',
    'initiator_select_passive_target',
    'initiator_poll_target',
    'initiator_select_dep_target',
    'initiator_deselect_target',
    'initiator_transceive_bytes',
    'initiator_transceive_bits',
    'initiator_transceive_bytes_timed',
    'initiator_transceive_bits_timed',
    'initiator_target_is_present',
    'target_init',
    'target_send_bytes',
    'target_receive_bytes',
    'target_send_bits',
    'target_receive_bits',
    'device_set_property_bool',
    'device_set_property_int',
    'get_supported_modulation',
    'get_supported_baud_rate',
    'device_get_information_about',
    'abort_command',
    'idle',
    'powerdown',
]
struct_nfc_driver._fields_ = [
    ('name', String),
    ('scan_type', scan_type_enum),
    ('scan', CFUNCTYPE(UNCHECKED(c_size_t), POINTER(nfc_context), POINTER(nfc_connstring), c_size_t)),
    ('open', CFUNCTYPE(UNCHECKED(POINTER(struct_nfc_device)), POINTER(nfc_context), nfc_connstring)),
    ('close', CFUNCTYPE(UNCHECKED(None), POINTER(struct_nfc_device))),
    ('strerror', CFUNCTYPE(UNCHECKED(c_char_p), POINTER(struct_nfc_device))),
    ('initiator_init', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device))),
    ('initiator_init_secure_element', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device))),
    ('initiator_select_passive_target', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), nfc_modulation, POINTER(c_uint8), c_size_t, POINTER(nfc_target))),
    ('initiator_poll_target', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), POINTER(nfc_modulation), c_size_t, c_uint8, c_uint8, POINTER(nfc_target))),
    ('initiator_select_dep_target', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), nfc_dep_mode, nfc_baud_rate, POINTER(nfc_dep_info), POINTER(nfc_target), c_int)),
    ('initiator_deselect_target', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device))),
    ('initiator_transceive_bytes', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8), c_size_t, c_int)),
    ('initiator_transceive_bits', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8))),
    ('initiator_transceive_bytes_timed', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8), c_size_t, POINTER(c_uint32))),
    ('initiator_transceive_bits_timed', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint32))),
    ('initiator_target_is_present', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), POINTER(nfc_target))),
    ('target_init', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), POINTER(nfc_target), POINTER(c_uint8), c_size_t, c_int)),
    ('target_send_bytes', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, c_int)),
    ('target_receive_bytes', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, c_int)),
    ('target_send_bits', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8))),
    ('target_receive_bits', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8))),
    ('device_set_property_bool', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), nfc_property, c_bool)),
    ('device_set_property_int', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), nfc_property, c_int)),
    ('get_supported_modulation', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), nfc_mode, POINTER(POINTER(nfc_modulation_type)))),
    ('get_supported_baud_rate', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), nfc_modulation_type, POINTER(POINTER(nfc_baud_rate)))),
    ('device_get_information_about', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), POINTER(POINTER(c_char)))),
    ('abort_command', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device))),
    ('idle', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device))),
    ('powerdown', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device))),
]

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/../nfc-internal.h: 164
class struct_nfc_user_defined_device(Structure):
    pass

struct_nfc_user_defined_device.__slots__ = [
    'name',
    'connstring',
    'optional',
]
struct_nfc_user_defined_device._fields_ = [
    ('name', c_char * int(256)),
    ('connstring', nfc_connstring),
    ('optional', c_bool),
]

struct_nfc_context.__slots__ = [
    'allow_autoscan',
    'allow_intrusive_scan',
    'log_level',
    'user_defined_devices',
    'user_defined_device_count',
]
struct_nfc_context._fields_ = [
    ('allow_autoscan', c_bool),
    ('allow_intrusive_scan', c_bool),
    ('log_level', c_uint32),
    ('user_defined_devices', struct_nfc_user_defined_device * int(4)),
    ('user_defined_device_count', c_uint),
]

struct_nfc_device.__slots__ = [
    'context',
    'driver',
    'driver_data',
    'chip_data',
    'name',
    'connstring',
    'bCrc',
    'bPar',
    'bEasyFraming',
    'bInfiniteSelect',
    'bAutoIso14443_4',
    'btSupportByte',
    'last_error',
]
struct_nfc_device._fields_ = [
    ('context', POINTER(nfc_context)),
    ('driver', POINTER(struct_nfc_driver)),
    ('driver_data', POINTER(None)),
    ('chip_data', POINTER(None)),
    ('name', c_char * int(256)),
    ('connstring', nfc_connstring),
    ('bCrc', c_bool),
    ('bPar', c_bool),
    ('bEasyFraming', c_bool),
    ('bInfiniteSelect', c_bool),
    ('bAutoIso14443_4', c_bool),
    ('btSupportByte', c_uint8),
    ('last_error', c_int),
]

enum_anon_37 = c_int# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x-internal.h: 136

pn53x_type = enum_anon_37# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x-internal.h: 136

enum_anon_38 = c_int# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 130

NORMAL = 0# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 130

POWERDOWN = (NORMAL + 1)# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 130

LOWVBAT = (POWERDOWN + 1)# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 130

pn53x_power_mode = enum_anon_38# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 130

enum_anon_39 = c_int# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 140

IDLE = 0# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 140

INITIATOR = (IDLE + 1)# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 140

TARGET = (INITIATOR + 1)# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 140

pn53x_operating_mode = enum_anon_39# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 140

enum_anon_40 = c_int# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 151

PSM_NORMAL = 1# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 151

PSM_VIRTUAL_CARD = 2# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 151

PSM_WIRED_CARD = 3# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 151

PSM_DUAL_CARD = 4# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 151

pn532_sam_mode = enum_anon_40# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 151

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 158
class struct_pn53x_io(Structure):
    pass

struct_pn53x_io.__slots__ = [
    'send',
    'receive',
]
struct_pn53x_io._fields_ = [
    ('send', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, c_int)),
    ('receive', CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, c_int)),
]

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 173
class struct_pn53x_data(Structure):
    pass

struct_pn53x_data.__slots__ = [
    'type',
    'firmware_text',
    'power_mode',
    'operating_mode',
    'current_target',
    'sam_mode',
    'io',
    'last_status_byte',
    'ui8TxBits',
    'ui8Parameters',
    'last_command',
    'timer_correction',
    'timer_prescaler',
    'wb_data',
    'wb_mask',
    'wb_trigged',
    'timeout_command',
    'timeout_atr',
    'timeout_communication',
    'supported_modulation_as_initiator',
    'supported_modulation_as_target',
]
struct_pn53x_data._fields_ = [
    ('type', pn53x_type),
    ('firmware_text', c_char * int(22)),
    ('power_mode', pn53x_power_mode),
    ('operating_mode', pn53x_operating_mode),
    ('current_target', POINTER(nfc_target)),
    ('sam_mode', pn532_sam_mode),
    ('io', POINTER(struct_pn53x_io)),
    ('last_status_byte', c_uint8),
    ('ui8TxBits', c_uint8),
    ('ui8Parameters', c_uint8),
    ('last_command', c_uint8),
    ('timer_correction', c_int16),
    ('timer_prescaler', c_uint16),
    ('wb_data', c_uint8 * int(((25406 - 25345) + 1))),
    ('wb_mask', c_uint8 * int(((25406 - 25345) + 1))),
    ('wb_trigged', c_bool),
    ('timeout_command', c_int),
    ('timeout_atr', c_int),
    ('timeout_communication', c_int),
    ('supported_modulation_as_initiator', POINTER(nfc_modulation_type)),
    ('supported_modulation_as_target', POINTER(nfc_modulation_type)),
]

enum_anon_41 = c_int# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 240

PM_UNDEFINED = (-1)# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 240

PM_ISO14443A_106 = 0# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 240

PM_FELICA_212 = 1# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 240

PM_FELICA_424 = 2# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 240

PM_ISO14443B_106 = 3# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 240

PM_JEWEL_106 = 4# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 240

PM_ISO14443B_212 = 6# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 240

PM_ISO14443B_424 = 7# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 240

PM_ISO14443B_847 = 8# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 240

pn53x_modulation = enum_anon_41# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 240

enum_anon_42 = c_int# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_UNDEFINED = (-1)# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_GENERIC_PASSIVE_106 = 0# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_GENERIC_PASSIVE_212 = 1# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_GENERIC_PASSIVE_424 = 2# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_ISO14443_4B_106 = 3# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_JEWEL_106 = 4# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_MIFARE = 16# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_FELICA_212 = 17# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_FELICA_424 = 18# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_ISO14443_4A_106 = 32# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_ISO14443_4B_TCL_106 = 35# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_DEP_PASSIVE_106 = 64# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_DEP_PASSIVE_212 = 65# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_DEP_PASSIVE_424 = 66# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_DEP_ACTIVE_106 = 128# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_DEP_ACTIVE_212 = 129# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

PTT_DEP_ACTIVE_424 = 130# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

pn53x_target_type = enum_anon_42# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 281

enum_anon_43 = c_int# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 296

PTM_NORMAL = 0# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 296

PTM_PASSIVE_ONLY = 1# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 296

PTM_DEP_ONLY = 2# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 296

PTM_ISO14443_4_PICC_ONLY = 4# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 296

pn53x_target_mode = enum_anon_43# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 296

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 298
for _lib in _libs.values():
    try:
        pn53x_ack_frame = (c_uint8 * int(6)).in_dll(_lib, "pn53x_ack_frame")
        break
    except:
        pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 299
for _lib in _libs.values():
    try:
        pn53x_nack_frame = (c_uint8 * int(6)).in_dll(_lib, "pn53x_nack_frame")
        break
    except:
        pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 301
for _lib in _libs.values():
    if not _lib.has("pn53x_init", "cdecl"):
        continue
    pn53x_init = _lib.get("pn53x_init", "cdecl")
    pn53x_init.argtypes = [POINTER(struct_nfc_device)]
    pn53x_init.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 302
if _libs["nfc"].has("pn53x_transceive", "cdecl"):
    pn53x_transceive = _libs["nfc"].get("pn53x_transceive", "cdecl")
    pn53x_transceive.argtypes = [POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8), c_size_t, c_int]
    pn53x_transceive.restype = c_int

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 304
for _lib in _libs.values():
    if not _lib.has("pn53x_set_parameters", "cdecl"):
        continue
    pn53x_set_parameters = _lib.get("pn53x_set_parameters", "cdecl")
    pn53x_set_parameters.argtypes = [POINTER(struct_nfc_device), c_uint8, c_bool]
    pn53x_set_parameters.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 305
for _lib in _libs.values():
    if not _lib.has("pn53x_set_tx_bits", "cdecl"):
        continue
    pn53x_set_tx_bits = _lib.get("pn53x_set_tx_bits", "cdecl")
    pn53x_set_tx_bits.argtypes = [POINTER(struct_nfc_device), c_uint8]
    pn53x_set_tx_bits.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 306
for _lib in _libs.values():
    if not _lib.has("pn53x_wrap_frame", "cdecl"):
        continue
    pn53x_wrap_frame = _lib.get("pn53x_wrap_frame", "cdecl")
    pn53x_wrap_frame.argtypes = [POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_uint8)]
    pn53x_wrap_frame.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 307
for _lib in _libs.values():
    if not _lib.has("pn53x_unwrap_frame", "cdecl"):
        continue
    pn53x_unwrap_frame = _lib.get("pn53x_unwrap_frame", "cdecl")
    pn53x_unwrap_frame.argtypes = [POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_uint8)]
    pn53x_unwrap_frame.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 308
for _lib in _libs.values():
    if not _lib.has("pn53x_decode_target_data", "cdecl"):
        continue
    pn53x_decode_target_data = _lib.get("pn53x_decode_target_data", "cdecl")
    pn53x_decode_target_data.argtypes = [POINTER(c_uint8), c_size_t, pn53x_type, nfc_modulation_type, POINTER(nfc_target_info)]
    pn53x_decode_target_data.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 311
if _libs["nfc"].has("pn53x_read_register", "cdecl"):
    pn53x_read_register = _libs["nfc"].get("pn53x_read_register", "cdecl")
    pn53x_read_register.argtypes = [POINTER(struct_nfc_device), c_uint16, POINTER(c_uint8)]
    pn53x_read_register.restype = c_int

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 312
if _libs["nfc"].has("pn53x_write_register", "cdecl"):
    pn53x_write_register = _libs["nfc"].get("pn53x_write_register", "cdecl")
    pn53x_write_register.argtypes = [POINTER(struct_nfc_device), c_uint16, c_uint8, c_uint8]
    pn53x_write_register.restype = c_int

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 313
for _lib in _libs.values():
    if not _lib.has("pn53x_decode_firmware_version", "cdecl"):
        continue
    pn53x_decode_firmware_version = _lib.get("pn53x_decode_firmware_version", "cdecl")
    pn53x_decode_firmware_version.argtypes = [POINTER(struct_nfc_device)]
    pn53x_decode_firmware_version.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 314
for _lib in _libs.values():
    if not _lib.has("pn53x_set_property_int", "cdecl"):
        continue
    pn53x_set_property_int = _lib.get("pn53x_set_property_int", "cdecl")
    pn53x_set_property_int.argtypes = [POINTER(struct_nfc_device), nfc_property, c_int]
    pn53x_set_property_int.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 315
for _lib in _libs.values():
    if not _lib.has("pn53x_set_property_bool", "cdecl"):
        continue
    pn53x_set_property_bool = _lib.get("pn53x_set_property_bool", "cdecl")
    pn53x_set_property_bool.argtypes = [POINTER(struct_nfc_device), nfc_property, c_bool]
    pn53x_set_property_bool.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 317
for _lib in _libs.values():
    if not _lib.has("pn53x_check_communication", "cdecl"):
        continue
    pn53x_check_communication = _lib.get("pn53x_check_communication", "cdecl")
    pn53x_check_communication.argtypes = [POINTER(struct_nfc_device)]
    pn53x_check_communication.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 318
for _lib in _libs.values():
    if not _lib.has("pn53x_idle", "cdecl"):
        continue
    pn53x_idle = _lib.get("pn53x_idle", "cdecl")
    pn53x_idle.argtypes = [POINTER(struct_nfc_device)]
    pn53x_idle.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 321
for _lib in _libs.values():
    if not _lib.has("pn53x_initiator_init", "cdecl"):
        continue
    pn53x_initiator_init = _lib.get("pn53x_initiator_init", "cdecl")
    pn53x_initiator_init.argtypes = [POINTER(struct_nfc_device)]
    pn53x_initiator_init.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 322
for _lib in _libs.values():
    if not _lib.has("pn532_initiator_init_secure_element", "cdecl"):
        continue
    pn532_initiator_init_secure_element = _lib.get("pn532_initiator_init_secure_element", "cdecl")
    pn532_initiator_init_secure_element.argtypes = [POINTER(struct_nfc_device)]
    pn532_initiator_init_secure_element.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 323
for _lib in _libs.values():
    if not _lib.has("pn53x_initiator_select_passive_target", "cdecl"):
        continue
    pn53x_initiator_select_passive_target = _lib.get("pn53x_initiator_select_passive_target", "cdecl")
    pn53x_initiator_select_passive_target.argtypes = [POINTER(struct_nfc_device), nfc_modulation, POINTER(c_uint8), c_size_t, POINTER(nfc_target)]
    pn53x_initiator_select_passive_target.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 327
for _lib in _libs.values():
    if not _lib.has("pn53x_initiator_poll_target", "cdecl"):
        continue
    pn53x_initiator_poll_target = _lib.get("pn53x_initiator_poll_target", "cdecl")
    pn53x_initiator_poll_target.argtypes = [POINTER(struct_nfc_device), POINTER(nfc_modulation), c_size_t, c_uint8, c_uint8, POINTER(nfc_target)]
    pn53x_initiator_poll_target.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 331
for _lib in _libs.values():
    if not _lib.has("pn53x_initiator_select_dep_target", "cdecl"):
        continue
    pn53x_initiator_select_dep_target = _lib.get("pn53x_initiator_select_dep_target", "cdecl")
    pn53x_initiator_select_dep_target.argtypes = [POINTER(struct_nfc_device), nfc_dep_mode, nfc_baud_rate, POINTER(nfc_dep_info), POINTER(nfc_target), c_int]
    pn53x_initiator_select_dep_target.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 336
for _lib in _libs.values():
    if not _lib.has("pn53x_initiator_transceive_bits", "cdecl"):
        continue
    pn53x_initiator_transceive_bits = _lib.get("pn53x_initiator_transceive_bits", "cdecl")
    pn53x_initiator_transceive_bits.argtypes = [POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)]
    pn53x_initiator_transceive_bits.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 338
for _lib in _libs.values():
    if not _lib.has("pn53x_initiator_transceive_bytes", "cdecl"):
        continue
    pn53x_initiator_transceive_bytes = _lib.get("pn53x_initiator_transceive_bytes", "cdecl")
    pn53x_initiator_transceive_bytes.argtypes = [POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8), c_size_t, c_int]
    pn53x_initiator_transceive_bytes.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 340
for _lib in _libs.values():
    if not _lib.has("pn53x_initiator_transceive_bits_timed", "cdecl"):
        continue
    pn53x_initiator_transceive_bits_timed = _lib.get("pn53x_initiator_transceive_bits_timed", "cdecl")
    pn53x_initiator_transceive_bits_timed.argtypes = [POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint32)]
    pn53x_initiator_transceive_bits_timed.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 342
for _lib in _libs.values():
    if not _lib.has("pn53x_initiator_transceive_bytes_timed", "cdecl"):
        continue
    pn53x_initiator_transceive_bytes_timed = _lib.get("pn53x_initiator_transceive_bytes_timed", "cdecl")
    pn53x_initiator_transceive_bytes_timed.argtypes = [POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8), c_size_t, POINTER(c_uint32)]
    pn53x_initiator_transceive_bytes_timed.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 344
for _lib in _libs.values():
    if not _lib.has("pn53x_initiator_deselect_target", "cdecl"):
        continue
    pn53x_initiator_deselect_target = _lib.get("pn53x_initiator_deselect_target", "cdecl")
    pn53x_initiator_deselect_target.argtypes = [POINTER(struct_nfc_device)]
    pn53x_initiator_deselect_target.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 345
for _lib in _libs.values():
    if not _lib.has("pn53x_initiator_target_is_present", "cdecl"):
        continue
    pn53x_initiator_target_is_present = _lib.get("pn53x_initiator_target_is_present", "cdecl")
    pn53x_initiator_target_is_present.argtypes = [POINTER(struct_nfc_device), POINTER(nfc_target)]
    pn53x_initiator_target_is_present.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 348
for _lib in _libs.values():
    if not _lib.has("pn53x_target_init", "cdecl"):
        continue
    pn53x_target_init = _lib.get("pn53x_target_init", "cdecl")
    pn53x_target_init.argtypes = [POINTER(struct_nfc_device), POINTER(nfc_target), POINTER(c_uint8), c_size_t, c_int]
    pn53x_target_init.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 349
for _lib in _libs.values():
    if not _lib.has("pn53x_target_receive_bits", "cdecl"):
        continue
    pn53x_target_receive_bits = _lib.get("pn53x_target_receive_bits", "cdecl")
    pn53x_target_receive_bits.argtypes = [POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8)]
    pn53x_target_receive_bits.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 350
for _lib in _libs.values():
    if not _lib.has("pn53x_target_receive_bytes", "cdecl"):
        continue
    pn53x_target_receive_bytes = _lib.get("pn53x_target_receive_bytes", "cdecl")
    pn53x_target_receive_bytes.argtypes = [POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, c_int]
    pn53x_target_receive_bytes.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 351
for _lib in _libs.values():
    if not _lib.has("pn53x_target_send_bits", "cdecl"):
        continue
    pn53x_target_send_bits = _lib.get("pn53x_target_send_bits", "cdecl")
    pn53x_target_send_bits.argtypes = [POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, POINTER(c_uint8)]
    pn53x_target_send_bits.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 352
for _lib in _libs.values():
    if not _lib.has("pn53x_target_send_bytes", "cdecl"):
        continue
    pn53x_target_send_bytes = _lib.get("pn53x_target_send_bytes", "cdecl")
    pn53x_target_send_bytes.argtypes = [POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t, c_int]
    pn53x_target_send_bytes.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 355
for _lib in _libs.values():
    if not _lib.has("pn53x_strerror", "cdecl"):
        continue
    pn53x_strerror = _lib.get("pn53x_strerror", "cdecl")
    pn53x_strerror.argtypes = [POINTER(struct_nfc_device)]
    pn53x_strerror.restype = c_char_p
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 358
for _lib in _libs.values():
    if not _lib.has("pn53x_SetParameters", "cdecl"):
        continue
    pn53x_SetParameters = _lib.get("pn53x_SetParameters", "cdecl")
    pn53x_SetParameters.argtypes = [POINTER(struct_nfc_device), c_uint8]
    pn53x_SetParameters.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 359
if _libs["nfc"].has("pn532_SAMConfiguration", "cdecl"):
    pn532_SAMConfiguration = _libs["nfc"].get("pn532_SAMConfiguration", "cdecl")
    pn532_SAMConfiguration.argtypes = [POINTER(struct_nfc_device), pn532_sam_mode, c_int]
    pn532_SAMConfiguration.restype = c_int

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 360
for _lib in _libs.values():
    if not _lib.has("pn53x_PowerDown", "cdecl"):
        continue
    pn53x_PowerDown = _lib.get("pn53x_PowerDown", "cdecl")
    pn53x_PowerDown.argtypes = [POINTER(struct_nfc_device)]
    pn53x_PowerDown.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 361
for _lib in _libs.values():
    if not _lib.has("pn53x_InListPassiveTarget", "cdecl"):
        continue
    pn53x_InListPassiveTarget = _lib.get("pn53x_InListPassiveTarget", "cdecl")
    pn53x_InListPassiveTarget.argtypes = [POINTER(struct_nfc_device), pn53x_modulation, c_uint8, POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_size_t), c_int]
    pn53x_InListPassiveTarget.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 365
for _lib in _libs.values():
    if not _lib.has("pn53x_InDeselect", "cdecl"):
        continue
    pn53x_InDeselect = _lib.get("pn53x_InDeselect", "cdecl")
    pn53x_InDeselect.argtypes = [POINTER(struct_nfc_device), c_uint8]
    pn53x_InDeselect.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 366
for _lib in _libs.values():
    if not _lib.has("pn53x_InRelease", "cdecl"):
        continue
    pn53x_InRelease = _lib.get("pn53x_InRelease", "cdecl")
    pn53x_InRelease.argtypes = [POINTER(struct_nfc_device), c_uint8]
    pn53x_InRelease.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 367
for _lib in _libs.values():
    if not _lib.has("pn53x_InAutoPoll", "cdecl"):
        continue
    pn53x_InAutoPoll = _lib.get("pn53x_InAutoPoll", "cdecl")
    pn53x_InAutoPoll.argtypes = [POINTER(struct_nfc_device), POINTER(pn53x_target_type), c_size_t, c_uint8, c_uint8, POINTER(nfc_target), c_int]
    pn53x_InAutoPoll.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 370
for _lib in _libs.values():
    if not _lib.has("pn53x_InJumpForDEP", "cdecl"):
        continue
    pn53x_InJumpForDEP = _lib.get("pn53x_InJumpForDEP", "cdecl")
    pn53x_InJumpForDEP.argtypes = [POINTER(struct_nfc_device), nfc_dep_mode, nfc_baud_rate, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), c_size_t, POINTER(nfc_target), c_int]
    pn53x_InJumpForDEP.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 377
for _lib in _libs.values():
    if not _lib.has("pn53x_TgInitAsTarget", "cdecl"):
        continue
    pn53x_TgInitAsTarget = _lib.get("pn53x_TgInitAsTarget", "cdecl")
    pn53x_TgInitAsTarget.argtypes = [POINTER(struct_nfc_device), pn53x_target_mode, POINTER(c_uint8), POINTER(c_uint8), c_size_t, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), c_size_t, POINTER(c_uint8), c_size_t, POINTER(c_uint8), c_int]
    pn53x_TgInitAsTarget.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 385
for _lib in _libs.values():
    if not _lib.has("pn53x_RFConfiguration__RF_field", "cdecl"):
        continue
    pn53x_RFConfiguration__RF_field = _lib.get("pn53x_RFConfiguration__RF_field", "cdecl")
    pn53x_RFConfiguration__RF_field.argtypes = [POINTER(struct_nfc_device), c_bool]
    pn53x_RFConfiguration__RF_field.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 386
for _lib in _libs.values():
    if not _lib.has("pn53x_RFConfiguration__Various_timings", "cdecl"):
        continue
    pn53x_RFConfiguration__Various_timings = _lib.get("pn53x_RFConfiguration__Various_timings", "cdecl")
    pn53x_RFConfiguration__Various_timings.argtypes = [POINTER(struct_nfc_device), c_uint8, c_uint8]
    pn53x_RFConfiguration__Various_timings.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 387
for _lib in _libs.values():
    if not _lib.has("pn53x_RFConfiguration__MaxRtyCOM", "cdecl"):
        continue
    pn53x_RFConfiguration__MaxRtyCOM = _lib.get("pn53x_RFConfiguration__MaxRtyCOM", "cdecl")
    pn53x_RFConfiguration__MaxRtyCOM.argtypes = [POINTER(struct_nfc_device), c_uint8]
    pn53x_RFConfiguration__MaxRtyCOM.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 388
for _lib in _libs.values():
    if not _lib.has("pn53x_RFConfiguration__MaxRetries", "cdecl"):
        continue
    pn53x_RFConfiguration__MaxRetries = _lib.get("pn53x_RFConfiguration__MaxRetries", "cdecl")
    pn53x_RFConfiguration__MaxRetries.argtypes = [POINTER(struct_nfc_device), c_uint8, c_uint8, c_uint8]
    pn53x_RFConfiguration__MaxRetries.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 391
for _lib in _libs.values():
    if not _lib.has("pn53x_check_ack_frame", "cdecl"):
        continue
    pn53x_check_ack_frame = _lib.get("pn53x_check_ack_frame", "cdecl")
    pn53x_check_ack_frame.argtypes = [POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t]
    pn53x_check_ack_frame.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 392
for _lib in _libs.values():
    if not _lib.has("pn53x_check_error_frame", "cdecl"):
        continue
    pn53x_check_error_frame = _lib.get("pn53x_check_error_frame", "cdecl")
    pn53x_check_error_frame.argtypes = [POINTER(struct_nfc_device), POINTER(c_uint8), c_size_t]
    pn53x_check_error_frame.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 393
for _lib in _libs.values():
    if not _lib.has("pn53x_build_frame", "cdecl"):
        continue
    pn53x_build_frame = _lib.get("pn53x_build_frame", "cdecl")
    pn53x_build_frame.argtypes = [POINTER(c_uint8), POINTER(c_size_t), POINTER(c_uint8), c_size_t]
    pn53x_build_frame.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 394
for _lib in _libs.values():
    if not _lib.has("pn53x_get_supported_modulation", "cdecl"):
        continue
    pn53x_get_supported_modulation = _lib.get("pn53x_get_supported_modulation", "cdecl")
    pn53x_get_supported_modulation.argtypes = [POINTER(nfc_device), nfc_mode, POINTER(POINTER(nfc_modulation_type))]
    pn53x_get_supported_modulation.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 395
for _lib in _libs.values():
    if not _lib.has("pn53x_get_supported_baud_rate", "cdecl"):
        continue
    pn53x_get_supported_baud_rate = _lib.get("pn53x_get_supported_baud_rate", "cdecl")
    pn53x_get_supported_baud_rate.argtypes = [POINTER(nfc_device), nfc_modulation_type, POINTER(POINTER(nfc_baud_rate))]
    pn53x_get_supported_baud_rate.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 396
for _lib in _libs.values():
    if not _lib.has("pn53x_get_information_about", "cdecl"):
        continue
    pn53x_get_information_about = _lib.get("pn53x_get_information_about", "cdecl")
    pn53x_get_information_about.argtypes = [POINTER(nfc_device), POINTER(POINTER(c_char))]
    pn53x_get_information_about.restype = c_int
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 398
for _lib in _libs.values():
    if not _lib.has("pn53x_data_new", "cdecl"):
        continue
    pn53x_data_new = _lib.get("pn53x_data_new", "cdecl")
    pn53x_data_new.argtypes = [POINTER(struct_nfc_device), POINTER(struct_pn53x_io)]
    pn53x_data_new.restype = POINTER(c_ubyte)
    pn53x_data_new.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 399
for _lib in _libs.values():
    if not _lib.has("pn53x_data_free", "cdecl"):
        continue
    pn53x_data_free = _lib.get("pn53x_data_free", "cdecl")
    pn53x_data_free.argtypes = [POINTER(struct_nfc_device)]
    pn53x_data_free.restype = None
    break

# /usr/include/nfc/nfc-types.h: 41
try:
    NFC_BUFSIZE_CONNSTRING = 1024
except:
    pass

# /usr/include/nfc/nfc.h: 72
try:
    __has_attribute_nonnull = 1
except:
    pass

# /usr/include/nfc/nfc.h: 156
try:
    NFC_SUCCESS = 0
except:
    pass

# /usr/include/nfc/nfc.h: 161
try:
    NFC_EIO = (-1)
except:
    pass

# /usr/include/nfc/nfc.h: 166
try:
    NFC_EINVARG = (-2)
except:
    pass

# /usr/include/nfc/nfc.h: 171
try:
    NFC_EDEVNOTSUPP = (-3)
except:
    pass

# /usr/include/nfc/nfc.h: 176
try:
    NFC_ENOTSUCHDEV = (-4)
except:
    pass

# /usr/include/nfc/nfc.h: 181
try:
    NFC_EOVFLOW = (-5)
except:
    pass

# /usr/include/nfc/nfc.h: 186
try:
    NFC_ETIMEOUT = (-6)
except:
    pass

# /usr/include/nfc/nfc.h: 191
try:
    NFC_EOPABORTED = (-7)
except:
    pass

# /usr/include/nfc/nfc.h: 196
try:
    NFC_ENOTIMPL = (-8)
except:
    pass

# /usr/include/nfc/nfc.h: 201
try:
    NFC_ETGRELEASED = (-10)
except:
    pass

# /usr/include/nfc/nfc.h: 206
try:
    NFC_ERFTRANS = (-20)
except:
    pass

# /usr/include/nfc/nfc.h: 211
try:
    NFC_EMFCAUTHFAIL = (-30)
except:
    pass

# /usr/include/nfc/nfc.h: 216
try:
    NFC_ESOFT = (-80)
except:
    pass

# /usr/include/nfc/nfc.h: 221
try:
    NFC_ECHIP = (-90)
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x-internal.h: 239
try:
    PN53X_REG_CIU_Mode = 25345
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x-internal.h: 300
try:
    PN53X_REG_CIU_Coll = 25406
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 40
try:
    SYMBOL_TX_CRC_ENABLE = 128
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 41
try:
    SYMBOL_TX_SPEED = 112
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 47
try:
    SYMBOL_TX_FRAMING = 3
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 50
try:
    SYMBOL_CURLIMOFF = 8
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 51
try:
    SYMBOL_SIC_SWITCH_EN = 16
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 52
try:
    SYMBOL_RANDOM_DATAREADY = 2
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 55
try:
    SYMBOL_RX_CRC_ENABLE = 128
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 56
try:
    SYMBOL_RX_SPEED = 112
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 57
try:
    SYMBOL_RX_NO_ERROR = 8
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 58
try:
    SYMBOL_RX_MULTIPLE = 4
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 60
try:
    SYMBOL_RX_FRAMING = 3
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 63
try:
    SYMBOL_FORCE_100_ASK = 64
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 64
try:
    SYMBOL_AUTO_WAKE_UP = 32
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 65
try:
    SYMBOL_INITIAL_RF_ON = 4
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 68
try:
    SYMBOL_PARITY_DISABLE = 16
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 71
try:
    SYMBOL_TAUTO = 128
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 72
try:
    SYMBOL_TPRESCALERHI = 15
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 75
try:
    SYMBOL_TPRESCALERLO = 255
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 78
try:
    SYMBOL_COMMAND = 15
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 79
try:
    SYMBOL_COMMAND_TRANSCEIVE = 12
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 82
try:
    SYMBOL_MF_CRYPTO1_ON = 8
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 85
try:
    SYMBOL_FLUSH_BUFFER = 128
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 86
try:
    SYMBOL_FIFO_LEVEL = 127
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 89
try:
    SYMBOL_INITIATOR = 16
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 90
try:
    SYMBOL_RX_LAST_BITS = 7
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 93
try:
    SYMBOL_START_SEND = 128
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 94
try:
    SYMBOL_RX_ALIGN = 112
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 95
try:
    SYMBOL_TX_LAST_BITS = 7
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 98
try:
    SUPPORT_ISO14443A = 1
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 99
try:
    SUPPORT_ISO14443B = 2
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 100
try:
    SUPPORT_ISO18092 = 4
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 103
try:
    PARAM_NONE = 0
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 104
try:
    PARAM_NAD_USED = 1
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 105
try:
    PARAM_DID_USED = 2
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 106
try:
    PARAM_AUTO_ATR_RES = 4
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 107
try:
    PARAM_AUTO_RATS = 16
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 108
try:
    PARAM_14443_4_PICC = 32
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 109
try:
    PARAM_NFC_SECURE = 32
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 110
try:
    PARAM_NO_AMBLE = 64
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 113
try:
    RFCI_FIELD = 1
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 114
try:
    RFCI_TIMING = 2
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 115
try:
    RFCI_RETRY_DATA = 4
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 116
try:
    RFCI_RETRY_SELECT = 5
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 117
try:
    RFCI_ANALOG_TYPE_A_106 = 10
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 118
try:
    RFCI_ANALOG_TYPE_A_212_424 = 11
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 119
try:
    RFCI_ANALOG_TYPE_B = 12
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 120
try:
    RFCI_ANALOG_TYPE_14443_4 = 13
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 164
try:
    PN53X_CACHE_REGISTER_MIN_ADDRESS = PN53X_REG_CIU_Mode
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 165
try:
    PN53X_CACHE_REGISTER_MAX_ADDRESS = PN53X_REG_CIU_Coll
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 166
try:
    PN53X_CACHE_REGISTER_SIZE = ((PN53X_CACHE_REGISTER_MAX_ADDRESS - PN53X_CACHE_REGISTER_MIN_ADDRESS) + 1)
except:
    pass

# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 215
def CHIP_DATA(pnd):
    return cast((pnd.contents.chip_data), POINTER(struct_pn53x_data))

nfc_emulator = struct_nfc_emulator# /home/jakob/git/pynfc/libnfc-1.7.1/include/nfc/nfc-emulation.h: 49

nfc_emulation_state_machine = struct_nfc_emulation_state_machine# /home/jakob/git/pynfc/libnfc-1.7.1/include/nfc/nfc-emulation.h: 59

pn53x_io = struct_pn53x_io# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 158

pn53x_data = struct_pn53x_data# /home/jakob/git/pynfc/libnfc-1.7.1/libnfc/chips/pn53x.h: 173

# No inserted files

# No prefix-stripping

