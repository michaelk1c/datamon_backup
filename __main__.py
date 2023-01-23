import os
import pandas as pd


DATAMON_MOUNT = "~/mnt/datamon"
FAIL = "\033[91m"
WARN = "\033[93m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
ENDC = "\033[0m"


def read_gsheet():
    try:
        sheet_id = "1cSySAbfm618mqP_U4iIf96xp1Zq-27Zg_e_bDjqTufU"
        sheet_name = "list"
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

        return pd.read_csv(url, keep_default_na=False)
    except Exception as err:
        print(err)


def mount_datamon(row):
    if row.bundle != "":
        cmd = f"datamon2 bundle mount --repo {row.name} --context {row.env} --bundle {row.bundle} --mount {DATAMON_MOUNT} --daemonize"
    else:
        cmd = f"datamon2 bundle mount --repo {row.name} --context {row.env} --label {row.label} --mount {DATAMON_MOUNT} --daemonize"

    print(f"{YELLOW}{cmd}{ENDC}")
    os.system(cmd)


def copy_data(row):
    bundle_label = row.bundle if row.bundle != "" else row.label
    dest_root = "~/mnt/bucket"
    dest = f"{dest_root}/{row.name}/{bundle_label}/"

    os.system(f"mkdir -p {dest}")

    cmd = f"rsync -avr {DATAMON_MOUNT}/ {dest}"
    print(f"{YELLOW}{cmd}{ENDC}")
    os.system(cmd)


def umount_datamon():
    cmd = f"umount {DATAMON_MOUNT}"
    print(f"{YELLOW}{cmd}{ENDC}")
    os.system(cmd)


def main():
    print(f"{CYAN}<<< run backup >>>{ENDC}")
    df = read_gsheet()

    # for row in df.iloc[:3].itertuples(index=False):
    for row in df.itertuples(index=False):
        try:
            print(f"#" * 10)
            mount_datamon(row)
            copy_data(row)
            umount_datamon()
        except Exception as err:
            print(err)


if __name__ == "__main__":
    main()
