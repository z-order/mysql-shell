/*
 * Copyright (c) 2016, Oracle and/or its affiliates. All rights reserved.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; version 2 of the
 * License.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301  USA
 */

// Interactive mysql_instance module for MySQL X sessions
// Exposed as "mysql_instance" in the shell

#ifndef _MOD_MYSQL_INSTANCE_H_
#define _MOD_MYSQL_INSTANCE_H_

#include "shellcore/module_registry.h"

namespace mysh
{
  namespace mysqlx
  {
    DECLARE_MODULE(MysqlInstance, mysql_instance);

    DECLARE_FUNCTION(validateInstance);
    DECLARE_FUNCTION(deployLocalInstance);

    shcore::Value validate_instance(const shcore::Argument_list &args);
    shcore::Value deploy_local_instance(const shcore::Argument_list &args);
    shcore::Value clone_instance(const shcore::Argument_list &args);
    shcore::Value configure_instance(const shcore::Argument_list &args);
    shcore::Value reset_instance(const shcore::Argument_list &args);

  protected:
    int get_default_instance_port() { return 3306; }

    END_DECLARE_MODULE();
  }
}

#endif
