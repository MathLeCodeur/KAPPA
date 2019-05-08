#!/bin/bash

ui_files="res/ui/*.ui"
rc_files=""
src_ui_dir="src/ui/generated/"

rm -rf ${src_ui_dir}*

for ui_file_path in $ui_files; do
    ui_file_full_name="$(basename $ui_file_path)"
    ui_file_name="${ui_file_full_name%.*}"
    ui_src_file_name="${src_ui_dir}${ui_file_name}_ui.py"

    pyuic5 $ui_file_path -o "$ui_src_file_name" --from-imports
    sed -i -e 's/\.\.\/icons/.\/res\/icons/g' "$ui_src_file_name"
done

for rc_file_path in $rc_files; do
    rc_file_full_name="$(basename $rc_file_path)"
    rc_file_name="${rc_file_full_name%.*}"
    rc_src_file_name="${src_ui_dir}${rc_file_name}_rc.py"

    pyrcc5 $rc_file_path -o "$rc_src_file_name"
done
