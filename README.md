# tutorial
tutorial about google style development utils

## protobuf
```bash
cd protobuf
bazel build :all
cd bazel-bin
./add_person_cpp addressbook.data
./list_people_cpp addressbook.data
```